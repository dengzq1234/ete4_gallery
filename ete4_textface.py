#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace


nw = '((A:1,B:1)internal_nodeF:1,(C:1,(D:1,E:1)internal_nodeG:1)internal_nodeH:1)root:1;'

t = Tree(nw, parser=1)

def get_face(prop):
    def layout_fn(node):
        if node.props.get(prop):
            if node.is_leaf:
                text_face = TextFace(
                node.props.get(prop)+'_aligned_column0', color='green',
                min_fsize=6, max_fsize=25, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
                node.add_face(text_face, position='aligned', column=0)
            else: # internal node or root
                text_face = TextFace(
                node.props.get(prop)+'_aligned_column1', color='green',
                min_fsize=6, max_fsize=25, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
                node.add_face(text_face, position='aligned', column=1)

                text_face = TextFace(
                node.props.get(prop)+'_aligned_column1_collapsed-only', color='green',
                min_fsize=6, max_fsize=25, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
                node.add_face(text_face, position='aligned', column=1, collapsed_only=True)

            text_face = TextFace(
                node.props.get(prop)+'_branch-right', color='red',
                min_fsize=6, max_fsize=25,  ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
            node.add_face(text_face, position='branch_right')

            text_face = TextFace(
                node.props.get(prop)+'_branch-top', color='blue',
                min_fsize=6, max_fsize=25, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
            node.add_face(text_face, position='branch_top')

            text_face = TextFace(
                node.props.get(prop)+'_branch-bottom', color='brown',
                min_fsize=6, max_fsize=25, ftype='sans-serif',
                padding_x=0, padding_y=0, width=None)
            node.add_face(text_face, position='branch_bottom')

    return layout_fn


layouts = [
    TreeLayout(name='text face with nodename', ns=get_face('name'), aligned_faces=True),
]
t.render("textface.png", dpi=300)
t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
