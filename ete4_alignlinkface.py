#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, AlignLinkFace

TREEFILE = 'example_data/tree.nw'

t = Tree(open(TREEFILE))
level = 2  # level 1 is leaf name


def layout_align_link(node):
    align_link_face = AlignLinkFace(
        stroke_color='blue', stroke_width=0.5, line_type=1, opacity=0.8)

    node.add_face(align_link_face,
                  position='branch_right',
                  column=1e9,
                  collapsed_only=not node.is_leaf)

layout_align_link.__name__ = 'Aligned panel link'
layout_align_link._module = 'default'


layouts = [
    TreeLayout(name='sample1', ns=layout_align_link, aligned_faces=True),
]

t.explore('example',layouts=layouts)
