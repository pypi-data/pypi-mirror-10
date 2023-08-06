#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""
Tests for a the pysemantic.utils module.
"""

import unittest
import os.path as op
from pysemantic.utils import colnames, get_md5_checksum


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.filepath = op.join(op.abspath(op.dirname(__file__)), "testdata",
                                "iris.csv")

    def test_colnames(self):
        ideal = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width',
                 'Species']
        actual = colnames(self.filepath)
        self.assertItemsEqual(actual, ideal)

    def test_md5(self):
        ideal = "9b3ecf3031979169c0ecc5e03cfe20a6"
        actual = get_md5_checksum(self.filepath)
        self.assertEqual(ideal, actual)

if __name__ == '__main__':
    unittest.main()
