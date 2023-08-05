# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

import warnings

from hypothesis.settings import Settings, Verbosity


class HypothesisDeprecationWarning(DeprecationWarning):
    pass


warnings.simplefilter('once', HypothesisDeprecationWarning)


def note_deprecation(message, settings):
    settings = settings or Settings.default
    warning = HypothesisDeprecationWarning(message)
    if settings.strict:
        raise warning
    elif settings.verbosity > Verbosity.quiet:
        warnings.warn(warning, stacklevel=3)
