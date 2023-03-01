#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, ArrowFace


TREEFILE = 'example_data/tree.nw'

popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2','sample3','sample4','sample5',
    'random_type','bool_type','bool_type2'
]

t = Tree(TREEFILE, format=1)
level = 2  # level 1 is leaf name


def layout_arrow(node):
    if not node.is_leaf():
        return

    face = ArrowFace(
        width=100, height=70, orientation='right',
        color='green', stroke_color='gray', stroke_width='1.5px',
        text=None, fgcolor='black',
        min_fsize=6, max_fsize=15,
        ftype='sans-serif',
        name='',
        padding_x=0, padding_y=0,
        tooltip=None)

    node.add_face(face, position='aligned', column=level)


layouts = [
    TreeLayout(name='sample1', ns=layout_arrow, aligned_faces=True),
]

t.explore(tree_name='example', layouts=layouts, popup_prop_keys=popup_prop_keys)
