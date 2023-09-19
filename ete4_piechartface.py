#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, PieChartFace, StackedBarFace

TREEFILE = 'example_data/tree.nw'

t = Tree(open(TREEFILE))

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

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
