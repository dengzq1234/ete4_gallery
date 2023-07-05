#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, CircleFace

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


layouts = [
    TreeLayout(name='sample1', ns=get_face('sample1'), aligned_faces=True),
]

t.explore('example', layouts=layouts, daemon=False)
