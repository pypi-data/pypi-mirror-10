#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@schrodinger.local>
#
# Distributed under terms of the MIT license.

"""Errors."""


class MissingProject(Exception):

    """Error raised when project is not found."""


class MissingConfigError(Exception):

    """Error raised when the pysemantic configuration file is not found."""
