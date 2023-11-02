#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, PieChartFace, StackedBarFace

TREEFILE = 'example_data/tree.nw'

<<<<<<< HEAD
popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2', 'sample3', 'sample4', 'sample5',
    'random_type', 'bool_type', 'bool_type2'
]

t = Tree(open(TREEFILE))
level = 2  # level 1 is leaf name
=======
t = Tree(open(TREEFILE))
>>>>>>> 3d1e59cab10e9cdd815ee5a6c879c957453a488f

def get_piechartface(prop):
    def layout_fn(node):
        if node.is_leaf:
            piechart_data = [
                ['pie1', 4, 'red', None],
                ['pie2', 10, 'blue', None],
                ['pie3', 20, 'green', None],
            ]
            face = PieChartFace(radius=30, data=piechart_data, name=prop,
                                padding_x=2, padding_y=2, tooltip=None)
            node.add_face(face, position='aligned')

    return layout_fn

def get_stackedbarface(prop):
    def layout_fn(node):
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

    return layout_fn

layouts = [
    TreeLayout(name='sample1', ns=get_piechartface('sample1'), aligned_faces=True),
    TreeLayout(name='sample2', ns=get_stackedbarface('sample2'), aligned_faces=True),
]

<<<<<<< HEAD
t.explore(daemon=False, layouts=layouts, compress=False)
=======
t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
>>>>>>> 3d1e59cab10e9cdd815ee5a6c879c957453a488f
