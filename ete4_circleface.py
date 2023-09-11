#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, CircleFace, RectFace

TREEFILE = 'example_data/tree.nw'

t = Tree(open(TREEFILE))


def get_face(prop):
    def layout_fn(node):
        if node.is_leaf:
            node_prop = float(node.props.get(prop)) * 15
            face = CircleFace(
                radius=node_prop, color='red', name=prop,
                padding_x=2, padding_y=2, tooltip=None)
            node.add_face(face, position='aligned', column=1)

    return layout_fn

def layout_rect(node):
    if not node.is_leaf:
        return

    rect_face = RectFace(
        width=50, height=50, color='blue',
        opacity=0.7, text="Rectangle", fgcolor='black',
        min_fsize=6, max_fsize=15, ftype='sans-serif',
        padding_x=0, padding_y=0,
        tooltip=None)

    node.add_face(rect_face, position='aligned', column=0)

layouts = [
    TreeLayout(name='rect', ns=layout_rect, aligned_faces=True),
    TreeLayout(name='circle', ns=get_face('sample1'), aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
