#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    15.10.2014 14:49:25 CEST
# File:    tb_hamilton.py

from common import *

import numpy as np

class TbHamiltonTestCase(CommonTestCase):

    def testH(self):
        H = z2pack.tb.Hamilton()

        # create the two atoms
        H.add_atom(([1, 1], 1), [0, 0, 0])
        H.add_atom(([-1, -1, 3], 1), [0.5, 0.6, 0.2])

        # add hopping between different atoms
        H.add_hopping(((0, 0), (1, 2)),
                      z2pack.tb.vectors.combine([0, -1], [0, -1], 0),
                      0.1,
                      phase=[1, -1j, 1j, -1])
        H.add_hopping(((0, 1), (1, 0)),
                      z2pack.tb.vectors.combine([0, -1], [0, -1], 0),
                      0.7,
                      phase=[1, 1j, -1j, -1])

        # add hopping between neighbouring orbitals of the same type
        H.add_hopping((((0, 0), (0, 0)), ((0, 1), (0, 1))),
                      z2pack.tb.vectors.neighbours([0, 1], forward_only=True),
                      -0.3,
                      phase=[1])
        H.add_hopping((((1, 1), (1, 1)), ((1, 0), (1, 0))),
                      z2pack.tb.vectors.neighbours([0, 1], forward_only=True),
                      -0.8,
                      phase=[1])
        H.add_hopping((((1, 1), (1, 1)), ((1, 0), (1, 0))),
                      [[1, 2, 3]],
                      -0.9,
                      phase=[1])
        M = [[[(0.99536826328310157-0.064747464977345695j), 0j], [0j, (0.99452189536827329-0.10452846326765346j)]], [[(0.96762793769258637-0.077241421373816427j), 0j], [0j, (0.99452189536827329-0.10452846326765346j)]], [[(0.99500005547481751-0.087507074372473195j), 0j], [0j, (0.99452189536827329-0.10452846326765348j)]], [[(0.96265477496458007-0.073352627805504625j), 0j], [0j, (0.99452189536827329-0.10452846326765344j)]], [[(0.99536826328310146-0.064747464977345667j), 0j], [0j, (0.99452189536827329-0.10452846326765344j)]], [[(0.96762793769258637-0.07724142137381651j), 0j], [0j, (0.99452189536827329-0.1045284632676535j)]], [[(0.99500005547481751-0.087507074372473057j), 0j], [0j, (0.9945218953682734-0.10452846326765337j)]], [[(0.96265477496457996-0.073352627805504667j), 0j], [0j, (0.99452189536827329-0.1045284632676535j)]], [[(0.99536826328310168-0.064747464977345681j), 0j], [0j, (0.99452189536827329-0.1045284632676535j)]], [[(0.96762793769258637-0.077241421373816344j), 0j], [0j, (0.9945218953682734-0.10452846326765337j)]], [[(0.99500005547481751-0.087507074372473279j), 0j], [0j, (0.99452189536827329-0.1045284632676535j)]], [[(0.96265477496457996-0.073352627805504542j), 0j], [0j, (0.99452189536827329-0.1045284632676535j)]]]

        self.assertFullAlmostEqual(H._get_m([[0.4, 0, x] for x in np.linspace(0, 1, 13)]), M)

if __name__ == "__main__":
    unittest.main()
