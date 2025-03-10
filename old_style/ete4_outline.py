#!/usr/bin/env python3

import random

from ete4 import Tree
from ete4.smartview import TreeLayout, OutlineFace


t = Tree(open("example_data/tree.nw"),parser=1)
#t.populate(20, dist_fn=random.random, support_fn=random.random)
def layout_outline(node):
    color="green"
    if not node.is_root:
        face = OutlineFace(
            stroke_color='red',
            color='green',
            #collapsing_height=float("inf"),
            opacity=1.0, stroke_width=500)

        node.sm_style["draw_descendants"] = False
        node.sm_style["outline_color"] = 'green'

        node.add_face(face, position='branch_right', collapsed_only=True)


layouts = [
    TreeLayout(name='sample1', ns=layout_outline, aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
