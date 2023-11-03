#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, AlignLinkFace

t = Tree()
t.populate(20, random_branches=True)

level = 2  # level 1 is leaf name


def layout_align_link(node):
    align_link_face = AlignLinkFace(
        stroke_color='blue', stroke_width=0.5, line_type=1, opacity=0.8)

    node.add_face(align_link_face,
                  position='branch_right',
                  column=1e9,
                  collapsed_only=not node.is_leaf)
    return


layouts = [
    TreeLayout(name='alignlink', ns=layout_align_link, aligned_faces=True),
]

t.explore(layouts=layouts, keep_server=True)