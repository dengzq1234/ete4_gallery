#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace


TREEFILE = 'example_data/example_tree.nw'

t = Tree(open(TREEFILE))


def get_face(prop):
    def layout_fn(node):
        if node.props.get(prop):
            text_face = TextFace(
                node.props.get(prop)+'_aligned', color='green',
                min_fsize=6, max_fsize=15, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
            node.add_face(text_face, position='aligned')

            text_face = TextFace(
                node.props.get(prop)+'_branch-right', color='red',
                min_fsize=6, max_fsize=15, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
            node.add_face(text_face, position='branch_right')

            text_face = TextFace(
                node.props.get(prop)+'_branch-top', color='blue',
                min_fsize=6, max_fsize=15, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
            node.add_face(text_face, position='branch_top')

    return layout_fn


layouts = [
    TreeLayout(name='name', ns=get_face('name'), aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
