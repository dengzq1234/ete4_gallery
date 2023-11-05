#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, RectFace

t = Tree()
t.populate(20, random_branches=True)

def layout_barplot(node):
    if node.is_leaf:
        width = node.dist * 100
        rect_face = RectFace(
            width=width, height=70, color='skyblue',
            opacity=0.7, text=None, fgcolor='black',
            min_fsize=6, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0,
            tooltip=None)
        node.add_face(rect_face, position='aligned', column=0)
        return 

layouts = [
    TreeLayout(name='sample1',ns=layout_barplot, aligned_faces=True),
]

t.explore(layouts=layouts, keep_server=True)
