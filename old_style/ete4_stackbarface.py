#!/usr/bin/env python3

import random

from ete4 import Tree
from ete4.smartview import TreeLayout, StackedBarFace


t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)

def get_stackedbarface(node):
    if node.is_leaf:
        stackedbar_data = [
            ['pie1', 4, 'red', None],
            ['pie2', 10, 'blue', None],
            ['pie3', 20, 'green', None],
        ]
        stackedbar_face = StackedBarFace(width=80, height=None,
                                            data=stackedbar_data,
                                            padding_x=2, padding_y=2)
        node.add_face(stackedbar_face, position='aligned')

    return


layouts = [
    TreeLayout(name='sample1', ns=get_stackedbarface, aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
