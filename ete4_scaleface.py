#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, ScaleFace


TREEFILE = 'example_data/tree.nw'

popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2', 'sample3', 'sample4', 'sample5',
    'random_type', 'bool_type', 'bool_type2'
]

t = Tree(TREEFILE, format=1)
level = 2  # level 1 is leaf name


def layout_scale(node):
    if not node.is_leaf():
        return

    scale_face = ScaleFace(
        name='sample1', width=100, color='black',
        scale_range=(0, 100), tick_width=80, line_width=1,
        formatter='%.0f',
        min_fsize=6, max_fsize=12, ftype='sans-serif',
        padding_x=0, padding_y=0)

    node.add_face(scale_face, position='aligned', column=level)


layouts = [
    TreeLayout(name='sample1', ns=layout_scale, aligned_faces=True),
]

t.explore(tree_name='example', layouts=layouts, popup_prop_keys=popup_prop_keys)
