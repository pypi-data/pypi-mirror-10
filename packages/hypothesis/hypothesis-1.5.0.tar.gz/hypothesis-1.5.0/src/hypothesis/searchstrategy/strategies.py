# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

from random import Random
from collections import namedtuple

from hypothesis.errors import BadData, NoExamples, WrongFormat, \
    UnsatisfiedAssumption
from hypothesis.control import assume
from hypothesis.settings import Settings
from hypothesis.deprecation import note_deprecation
from hypothesis.internal.compat import hrange, integer_types
from hypothesis.utils.extmethod import ExtMethod
from hypothesis.internal.chooser import chooser


class StrategyExtMethod(ExtMethod):

    def __call__(self, specifier, settings=None):
        if isinstance(specifier, SearchStrategy):
            return specifier

        if settings is None:
            settings = Settings()

        note_deprecation((
            'Calling strategy with non-strategy object %s is deprecated '
            'and will be removed in Hypothesis 2.0. Use the functions in '
            'hypothesis.strategies instead.') % (
                repr(specifier),
        ), settings)

        result = super(StrategyExtMethod, self).__call__(specifier, settings)
        assert isinstance(result, SearchStrategy)
        return result


strategy = StrategyExtMethod()


Infinity = float('inf')
EFFECTIVELY_INFINITE = 2 ** 32


def infinitish(x):
    if x >= EFFECTIVELY_INFINITE:
        return Infinity
    else:
        return x


def check_type(typ, value, e=WrongFormat):
    if not isinstance(value, typ):
        if isinstance(typ, tuple):
            name = 'any of ' + ', '.join(t.__name__ for t in typ)
        else:
            name = typ.__name__
        raise e('Value %r is not an instance of %s' % (
            value, name
        ))


def check_data_type(typ, value):
    check_type(typ, value, BadData)


def check_length(l, value, e=BadData):
    try:
        actual = len(value)
    except TypeError:
        raise e('Expected type with length but got %r' % (value,))
    if actual != l:
        raise e('Expected %d elements but got %d from %r' % (
            l, actual, value
        ))


def one_of_strategies(xs):
    """Helper function for unioning multiple strategies."""
    xs = tuple(xs)
    if not xs:
        raise ValueError('Cannot join an empty list of strategies')
    if len(xs) == 1:
        return xs[0]
    return OneOfStrategy(xs)


class SearchStrategy(object):

    """A SearchStrategy is an object that knows how to explore data of a given
    type.

    Except where noted otherwise, methods on this class are not part of the
    public API and their behaviour may change significantly between minor
    version releases. They will generally be stable between patch releases.

    With that in mind, here is how SearchStrategy works.

    A search strategy is responsible for generating, simplifying and
    serializing examples for saving.

    In order to do this a strategy has three types (where type here is more
    precise than just the class of the value. For example a tuple of ints
    should be considered different from a tuple of strings):

    1. The strategy parameter type
    2. The strategy template type
    3. The generated type

    Of these, the first two should be considered to be private implementation
    details of a strategy and the only valid thing to do them is to pass them
    back to the search strategy. Additionally, templates may be compared for
    equality and hashed.

    Templates must be of quite a restricted type. A template may be any of the
    following:

    1. Any instance of the types bool, float, int, str (unicode on 2.7)
    2. None
    3. Any tuple or namedtuple of valid template types
    4. Any frozenset of valid template types

    This may be relaxed a bit in future, but the requirement that templates are
    hashable probably won't be.

    This may all seem overly complicated but it's for a fairly good reason.
    For more discussion of the motivation see
    http://hypothesis.readthedocs.org/en/master/internals.html

    Given these, data generation happens in three phases:

    1. Draw a parameter value from a random number (defined by
       draw_parameter)
    2. Given a parameter value and a Random, draw a random template
    3. Reify a template value, deterministically turning it into a value of
       the desired type.

    Data simplification proceeds on template values, taking a template and
    providing a generator over some examples of similar but simpler templates.

    """

    def example(self):
        """Provide an example of the sort of value that this strategy
        generates. This is biased to be slightly simpler than is typical for
        values from this strategy, for clarity purposes.

        This method shouldn't be taken too seriously. It's here for interactive
        exploration of the API, not for any sort of real testing.

        This method is part of the public API.

        """
        random = Random()

        parts = []

        for _ in hrange(20):
            if len(parts) >= 3:
                break
            try:
                template = self.draw_and_produce(random)
                reified = self.reify(template)
                parts.append((template, reified))
            except UnsatisfiedAssumption:
                pass
        if not parts:
            raise NoExamples(
                'Could not find any valid examples in 20 tries'
            )

        return min(parts, key=lambda tr: self.__template_size(tr[0]))[1]

    def map(self, pack):
        """Returns a new strategy that generates values by generating a value
        from this strategy and then calling pack() on the result, giving that.

        This method is part of the public API.

        """
        return MappedSearchStrategy(
            pack=pack, strategy=self
        )

    def flatmap(self, expand):
        """Returns a new strategy that generates values by generating a value
        from this strategy, say x, then generating a value from
        strategy(expand(x))

        This method is part of the public API.

        """
        return FlatMapStrategy(
            expand=expand, strategy=self
        )

    def filter(self, condition):
        """Returns a new strategy that generates values from this strategy
        which satisfy the provided condition. Note that if the condition is too
        hard to satisfy this might result in your tests failing with
        Unsatisfiable.

        This method is part of the public API.

        """
        return FilteredStrategy(
            condition=condition,
            strategy=self,
        )

    def __or__(self, other):
        """Return a strategy which produces values by randomly drawing from one
        of this strategy or the other strategy.

        This method is part of the public API.

        """
        if not isinstance(other, SearchStrategy):
            raise ValueError('Cannot | a SearchStrategy with %r' % (other,))
        return one_of_strategies((self, other))

    # HERE BE DRAGONS. All below is non-public API of varying degrees of
    # stability.

    # Methods to be overridden by subclasses

    def draw_parameter(self, random):
        """Produce a random valid parameter for this strategy, using only data
        from the provided random number generator."""
        raise NotImplementedError(  # pragma: no cover
            '%s.draw_parameter()' % (self.__class__.__name__))

    def draw_template(self, random, parameter_value):
        """Given this Random and this parameter value, produce a random valid
        template for this strategy."""
        raise NotImplementedError(  # pragma: no cover
            '%s.draw_template()' % (self.__class__.__name__))

    def reify(self, template):
        """Given a template value, deterministically convert it into a value of
        the desired final type."""
        raise NotImplementedError(  # pragma: no cover
            '%s.reify()' % (self.__class__.__name__))

    def to_basic(self, template):
        """Convert a template value for this strategy into basic data.

        Basic data is any of:

            1. A bool, None, an int that fits into 64 bits, or a unicode string
            2. A list of basic data

        """
        raise NotImplementedError(  # pragma: no cover
            '%s.to_basic()' % (self.__class__.__name__))

    def from_basic(self, value):
        """Convert basic data back to a template, raising BadData if the
        provided data cannot be converted into a valid template for this
        strategy.

        It is not required that from_basic(to_basic(template)) == template. It
        is however required that to_basic(from_basic(data)) == data (if this
        does not raise an exception).

        """
        raise NotImplementedError(  # pragma: no cover
            '%s.from_basic()' % (self.__class__.__name__))

    # Gory implementation details

    #: Provide an upper bound on the number of available templates.
    #: The intended interpretation is that template_upper_bound means "if
    #: you've only found this many templates don't worry about it". It is also
    #: used internally in a few places for certain optimisations.
    #: Generally speaking once this reaches numbers >= 2 ** 32 or so you might
    #: as well just return float('inf').
    #: Note that there may be more distinct templates than there are
    #: representable values, because some templates may not reify and some may
    #: lead to the same value.
    template_upper_bound = Infinity

    def __init__(self):
        pass

    def draw_and_produce(self, random):
        return self.draw_template(random, self.draw_parameter(random))

    def __template_size(self, template):
        """Gives an approximate estimate of how "large" this template value is.

        This doesn't really matter for anything, it's just a convenience
        used to implement example().

        """
        def basic_size(x):
            try:
                if len(x) == 1:
                    return 1
            except TypeError:
                return 1
            return sum(map(basic_size, x))
        return basic_size(self.to_basic(template))

    def strictly_simpler(self, x, y):
        """
        Is the left hand argument *strictly* simpler than the right hand side.

        Required properties:

        1. not strictly_simpler(x, y)
        2. not (strictly_simpler(x, y) and strictly_simpler(y, x))
        3. not (strictly_simpler(x, y) and strictly_simpler(y, z)
           and strictly_simpler(z x))

        This is used for hinting in certain cases. The default implementation
        of it always returns False and this is perfectly acceptable to leave
        as is.
        """
        return False

    def simplifiers(self, random, template):
        """Yield a sequence of functions which each take a Random object and a
        single template and produce a generator over "simpler" versions of that
        template.

        The only other required invariant that each simplifier must satisfy is
        it should not be the case that strictly_simpler(x, y) for any y in
        simplify(random, x). That is, it's OK if the simplify doesn't produce
        a strictly simpler value but it must not produce a strictly more
        complex one.

        General tips for a good simplify function:

            1. The generator shouldn't yield too many values. A few hundred is
               fine, but if you're generating millions of simplifications you
               may wish to reconsider your life choices and evaluate which ones
               actually matter to you.
            2. Cycles in simplify are fine, but the simplify graph should be
               bounded in the sense that there should be no infinite acyclic
               paths where a1 simplifies to a2 simplifies to ...
            3. Try major simplifications first to see if you get lucky. Yield
               a minimal element, throw out half of your data, etc. Providing
               shortcuts in the graph will speed up the simplification process
               a lot.

        The template argument is provided to allow picking simplifiers that are
        likely to be useful. It should be considered only a hint, and each
        simplifier must be valid (in the sense of not erroring. It doesn't have
        to do anything useful) for all templates valid for this strategy.

        By default this just yields the basic_simplify function (which in turn
        by default does not do anything useful). If you override this function
        and also override basic_simplify you should make sure to yield it, or
        it will not be called.

        """
        yield self.basic_simplify

    def full_simplify(self, random, template):
        """A convenience method.

        Run each simplifier over this template and yield the results in
        turn.

        The order in which simplifiers are run is lightly randomized from the
        order in which simplifiers provides them, in order to avoid certain
        pathological cases.

        """
        saved_for_later = []
        for simplifier in self.simplifiers(random, template):
            if random.randint(0, 1):
                for value in simplifier(random, template):
                    yield value
            else:
                saved_for_later.append(simplifier)
        random.shuffle(saved_for_later)
        for simplifier in saved_for_later:
            for value in simplifier(random, template):
                yield value

    def basic_simplify(self, random, template):
        """A convenience method for subclasses that do not have complex
        simplification requirements to override.

        See simplifiers for details.

        """
        return iter(())


class OneOfStrategy(SearchStrategy):

    """Implements a union of strategies. Given a number of strategies this
    generates values which could have come from any of them.

    The conditional distribution draws uniformly at random from some non-empty
    subset of these strategies and then draws from the conditional distribution
    of that strategy.

    """

    Parameter = namedtuple(
        'Parameter', ('chooser', 'child_parameters')
    )

    def __init__(self,
                 strategies):
        SearchStrategy.__init__(self)
        strategies = tuple(strategies)
        if len(strategies) <= 1:
            raise ValueError('Need at least 2 strategies to choose amongst')
        self.element_strategies = list(strategies)
        self.template_upper_bound = 0
        for e in self.element_strategies:
            self.template_upper_bound += e.template_upper_bound
        self.template_upper_bound = infinitish(self.template_upper_bound)

    def __repr__(self):
        return ' | '.join(map(repr, self.element_strategies))

    def strictly_simpler(self, x, y):
        lx, vx = x
        ly, vy = y
        if lx < ly:
            return True
        if lx > ly:
            return False
        return self.element_strategies[lx].strictly_simpler(vx, vy)

    def reify(self, value):
        s, x = value
        return self.element_strategies[s].reify(x)

    def draw_parameter(self, random):
        n = len(self.element_strategies)
        return self.Parameter(
            chooser=chooser(
                random.getrandbits(8) + 1 for _ in hrange(n)),
            child_parameters=[
                s.draw_parameter(random) for s in self.element_strategies]
        )

    def draw_template(self, random, pv):
        child = pv.chooser.choose(random)
        return (
            child,
            self.element_strategies[child].draw_template(
                random, pv.child_parameters[child]))

    def element_simplifier(self, s, simplifier):
        def accept(random, template):
            if template[0] != s:
                return
            for value in simplifier(random, template[1]):
                yield (s, value)
        accept.__name__ = str(
            'element_simplifier(%d, %s)' % (
                s, simplifier.__name__,
            )
        )
        return accept

    def simplifiers(self, random, template):
        i, value = template
        for simplify in self.element_strategies[i].simplifiers(random, value):
            yield self.element_simplifier(i, simplify)

    def to_basic(self, template):
        i, value = template
        return [i, self.element_strategies[i].to_basic(value)]

    def from_basic(self, data):
        check_data_type(list, data)
        check_length(2, data)
        i, value = data
        check_data_type(integer_types, i)
        if i < 0:
            raise BadData('Index out of range: %d < 0' % (i,))
        elif i >= len(self.element_strategies):
            raise BadData(
                'Index out of range: %d >= %d' % (
                    i, len(self.element_strategies)))

        return (i, self.element_strategies[i].from_basic(value))


class MappedSearchStrategy(SearchStrategy):

    """A strategy which is defined purely by conversion to and from another
    strategy.

    Its parameter and distribution come from that other strategy.

    """

    def __init__(self, strategy, pack=None):
        SearchStrategy.__init__(self)
        self.mapped_strategy = strategy
        self.template_upper_bound = self.mapped_strategy.template_upper_bound
        if pack is not None:
            self.pack = pack

    def __repr__(self):
        return 'MappedSearchStrategy(%r, %s)' % (
            self.mapped_strategy, getattr(
                self.pack, '__name__', type(self.pack).__name__))

    def draw_parameter(self, random):
        return self.mapped_strategy.draw_parameter(random)

    def draw_template(self, random, pv):
        return self.mapped_strategy.draw_template(random, pv)

    def pack(self, x):
        """Take a value produced by the underlying mapped_strategy and turn it
        into a value suitable for outputting from this strategy."""
        raise NotImplementedError(
            '%s.pack()' % (self.__class__.__name__))

    def reify(self, value):
        return self.pack(self.mapped_strategy.reify(value))

    def simplifiers(self, random, template):
        return self.mapped_strategy.simplifiers(random, template)

    def strictly_simpler(self, x, y):
        return self.mapped_strategy.strictly_simpler(x, y)

    def to_basic(self, template):
        return self.mapped_strategy.to_basic(template)

    def from_basic(self, data):
        return self.mapped_strategy.from_basic(data)


class FilteredStrategy(MappedSearchStrategy):

    def __init__(self, strategy, condition):
        super(FilteredStrategy, self).__init__(strategy=strategy)
        self.condition = condition

    def pack(self, value):
        assume(self.condition(value))
        return value


class FlatMapStrategy(SearchStrategy):
    TemplateFromSeed = namedtuple(
        'TemplateFromSeed', (
            'source_template', 'parameter_seed', 'template_seed',
        ))

    TemplateFromTemplate = namedtuple(
        'TemplateFromTemplate', (
            'source_template', 'parameter_seed', 'template_seed',
            'target_template',
        ))

    TemplateFromBasic = namedtuple(
        'TemplateFromBasic', (
            'source_template', 'parameter_seed', 'template_seed',
            'basic_data',
        ))

    def __repr__(self):
        return 'FlatMapStrategy(%r, %s)' % (
            self.flatmapped_strategy,
            getattr(self.expand, '__name__', type(self.expand).__name__)
        )

    def __init__(
        self, strategy, expand
    ):
        self.flatmapped_strategy = strategy
        self.expand = expand
        self.strategy_cache = {}

    def draw_parameter(self, random):
        return (
            self.flatmapped_strategy.draw_parameter(random),
            random.getrandbits(64),
        )

    def draw_template(self, random, parameter):
        source_template = self.flatmapped_strategy.draw_template(
            random, parameter[0])
        parameter_seed = random.getrandbits(64)
        template_seed = random.getrandbits(64)

        if source_template in self.strategy_cache:
            target = self.strategy_cache[source_template]
            target_parameter = target.draw_parameter(Random(parameter_seed))
            target_template = target.draw_template(
                Random(template_seed),
                target_parameter,
            )
            return self.TemplateFromTemplate(
                source_template=source_template,
                parameter_seed=parameter_seed,
                template_seed=template_seed,
                target_template=target_template,
            )
        else:
            return self.TemplateFromSeed(
                source_template=source_template,
                parameter_seed=parameter_seed,
                template_seed=template_seed,
            )

    def strictly_simpler(self, x, y):
        if self.flatmapped_strategy.strictly_simpler(
            x.source_template, y.source_template
        ):
            return True
        if self.flatmapped_strategy.strictly_simpler(
            y.source_template, x.source_template
        ):
            return False
        if x.source_template == y.source_template:
            if x.source_template in self.strategy_cache:
                strat = self.strategy_cache[x.source_template]
                return strat.strictly_simpler(
                    self.target_template(x),
                    self.target_template(y),
                )
            else:
                return x.template_seed < y.template_seed
        return False

    def simplifiers(self, random, template):
        for simplify in self.flatmapped_strategy.simplifiers(
            random,
            template.source_template
        ):
            yield self.left_simplifier(simplify)
        if template.source_template in self.strategy_cache:
            target_strategy = self.strategy_cache[template.source_template]
            target_template = self.target_template(template)
            for simplify in target_strategy.simplifiers(
                random, target_template
            ):
                yield self.right_simplifier(
                    template.source_template, simplify
                )

    def left_simplifier(self, simplify):
        def accept(random, template):
            for simpler in simplify(random, template.source_template):
                yield self.TemplateFromSeed(
                    source_template=simpler,
                    parameter_seed=template.parameter_seed,
                    template_seed=template.template_seed,
                )
        accept.__name__ = str(
            'left_simplifier(%s)' % (simplify.__name__,)
        )
        return accept

    def right_simplifier(self, source_template, simplify):
        def accept(random, template):
            if template.source_template != source_template:
                return
            for simpler in simplify(random, self.target_template(template)):
                yield self.TemplateFromTemplate(
                    source_template=source_template,
                    parameter_seed=template.parameter_seed,
                    template_seed=template.template_seed,
                    target_template=simpler,
                )
        accept.__name__ = str(
            'right_simplifier(%s)' % (simplify.__name__,)
        )
        return accept

    def target_template(self, template):
        assert template.source_template in self.strategy_cache
        target_strategy = self.strategy_cache[template.source_template]
        if isinstance(template, self.TemplateFromTemplate):
            return template.target_template
        elif isinstance(template, self.TemplateFromBasic):
            try:
                return target_strategy.from_basic(
                    listize_basic(template.basic_data)
                )
            except BadData:
                pass
        target_parameter = target_strategy.draw_parameter(
            Random(template.parameter_seed)
        )
        return target_strategy.draw_template(
            Random(template.template_seed),
            target_parameter,
        )

    def reify(self, template):
        source_template = template.source_template
        if source_template not in self.strategy_cache:
            target_strategy = strategy(self.expand(
                self.flatmapped_strategy.reify(source_template)
            ))
            self.strategy_cache[source_template] = target_strategy
        else:
            target_strategy = self.strategy_cache[source_template]
        return target_strategy.reify(self.target_template(template))

    def to_basic(self, template):
        bits = [
            self.flatmapped_strategy.to_basic(template.source_template),
            template.parameter_seed, template.template_seed
        ]
        if isinstance(template, self.TemplateFromBasic):
            bits.append(listize_basic(template.basic_data))
        elif isinstance(template, self.TemplateFromTemplate):
            target_strategy = self.strategy_cache[template.source_template]
            bits.append(target_strategy.to_basic(template.target_template))
        else:
            assert isinstance(template, self.TemplateFromSeed)
        return bits

    def from_basic(self, data):
        check_data_type(list, data)
        if len(data) < 3:
            raise BadData(
                'Too few elements. Expected 3 or 4 but got %d' % (len(data),)
            )
        if len(data) > 4:
            raise BadData(
                'Too many elements. Expected 3 or 4 but got %d' % (len(data),)
            )
        check_data_type(integer_types, data[1])
        check_data_type(integer_types, data[2])
        source_template = self.flatmapped_strategy.from_basic(data[0])
        if len(data) == 4:
            return self.TemplateFromBasic(
                source_template=source_template,
                parameter_seed=data[1], template_seed=data[2],
                basic_data=tupleize_basic(data[3])
            )
        else:
            assert len(data) == 3
            return self.TemplateFromSeed(
                source_template=source_template,
                parameter_seed=data[1], template_seed=data[2],
            )


def tupleize_basic(x):
    if isinstance(x, list):
        return tuple(map(tupleize_basic, x))
    else:
        return x


def listize_basic(x):
    if isinstance(x, tuple):
        return list(map(listize_basic, x))
    else:
        return x
