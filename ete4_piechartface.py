#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, PieChartFace


TREEFILE = 'example_data/tree.nw'

popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2', 'sample3', 'sample4', 'sample5',
    'random_type', 'bool_type', 'bool_type2'
]

t = Tree(open(TREEFILE))
level = 2  # level 1 is leaf name

def get_face(prop):
    def layout_fn(node):
        if node.is_leaf:
            piechart_data = [
                ['pie1', 4, 'red', None],
                ['pie2', 10, 'blue', None],
                ['pie3', 20, 'green', None],
            ]
            face = PieChartFace(radius=20, data=piechart_data, name=prop,
                                padding_x=2, padding_y=2, tooltip=None)
            node.add_face(face, position='aligned', column=level)

    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face('sample1'), aligned_faces=True),
]

t.explore(daemon=False, layouts=layouts, compress=False)
