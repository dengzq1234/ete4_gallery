#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, ArrowFace


TREEFILE = 'example_data/tree.nw'

t = Tree(open(TREEFILE))


def layout_arrow(node):
    if not node.is_leaf:
        return

    right_face = ArrowFace(
        width=100, height=70, orientation='right',
        color='black', stroke_color='gray', stroke_width='1.5px',
        text=None, fgcolor='black',
        min_fsize=6, max_fsize=15,
        ftype='sans-serif',
        name='',
        padding_x=0, padding_y=0,
        tooltip=None)

    left_face = ArrowFace(
        width=100, height=70, orientation='left',
        color='red', stroke_color='gray', stroke_width='1.5px',
        text=None, fgcolor='black',
        min_fsize=6, max_fsize=15,
        ftype='sans-serif',
        name='',
        padding_x=0, padding_y=0,
        tooltip=None)

    if node.name.endswith("FALPE"):
        node.add_face(left_face, position='aligned')
    else:
        node.add_face(right_face, position='aligned')

layouts = [
    TreeLayout(name='sample1', ns=layout_arrow, aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
