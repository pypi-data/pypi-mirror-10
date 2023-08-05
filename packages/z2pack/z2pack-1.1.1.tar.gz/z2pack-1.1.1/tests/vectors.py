#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    15.10.2014 10:20:25 CEST
# File:    vectors.py

from common import *


class TbVectorsTestCase(CommonTestCase):
    """
    tests for tb.vectors
    """

    def test_combine(self):
        self.assertFullEqual(
            z2pack.tb.vectors.combine(-1, [0, 3], [1, 2]),
            [[-1, 0, 1], [-1, 0, 2], [-1, 3, 1], [-1, 3, 2]])

        self.assertFullEqual(
            z2pack.tb.vectors.combine(0, 1, 2),
            [[0, 1, 2]])

        self.assertFullEqual(
            z2pack.tb.vectors.combine((0, 1), (2, 3), (4, 5)),
            [[0, 2, 4], [0, 2, 5], [0, 3, 4], [0, 3, 5], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5]])
                             
    def test_neighbours(self):
        self.assertFullEqual(
            z2pack.tb.vectors.neighbours([0, 1]),
            [[1, 0, 0], [0, 1, 0]])

        self.assertFullEqual(
            z2pack.tb.vectors.neighbours([0, 1], forward_only=False),
            [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]])

        self.assertFullEqual(
            z2pack.tb.vectors.neighbours([2, 0, 1], forward_only=False),
            [[0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]])

        self.assertFullEqual(
            z2pack.tb.vectors.neighbours([2, 0, 1]),
            [[0, 0, 1], [1, 0, 0], [0, 1, 0]])

        self.assertFullEqual(z2pack.tb.vectors.neighbours(1),
                             [[0, 1, 0]])

        self.assertRaises(TypeError, z2pack.tb.vectors.neighbours, [2, 0, 1.])

        self.assertRaises(TypeError, z2pack.tb.vectors.neighbours, 'str')

if __name__ == "__main__":
    unittest.main()
