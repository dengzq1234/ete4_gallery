#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace


TREEFILE = 'example_data/tree.nw'

t = Tree(TREEFILE, format=1)


def get_face(prop):
    def layout_fn(node):
        if node.is_leaf():
            text_face = TextFace(
                node.props.get(prop), color='black',
                min_fsize=6, max_fsize=15, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
            node.add_face(text_face, position='aligned')

    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face('sample1'), aligned_faces=True),
]

t.explore(tree_name='example', layouts=layouts)
