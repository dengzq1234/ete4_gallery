#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, PieChartFace, StackedBarFace

t = Tree()
t.populate(20, random_branches=True)


def get_piechartface(node):

    if node.is_leaf:
        piechart_data = [
            ['pie1', 4, 'red', None],
            ['pie2', 10, 'blue', None],
            ['pie3', 20, 'green', None],
        ]
        face = PieChartFace(radius=30, data=piechart_data, name="piechart",
                            padding_x=2, padding_y=2, tooltip=None)
        node.add_face(face, position='aligned')

    return

layouts = [
    TreeLayout(name="piechart", ns=get_piechartface, aligned_faces=True),

]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
