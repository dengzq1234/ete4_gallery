#!/usr/bin/env python3

import os

from ete4 import Tree
from ete4.smartview import TreeLayout, ImgFace


TREEFILE = 'example_data/tree.nw'
ABSOLUTE_IMGPATH = os.path.abspath('example_data/frog.jpeg')

t = Tree(open(TREEFILE))


def get_face(prop):
    def layout_fn(node):
        if node.is_leaf:
            face = ImgFace(
                img_path=ABSOLUTE_IMGPATH, width=70, height=50, name='',
                padding_x=0, padding_y=0)
            node.add_face(face, position='aligned')

    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face('sample1'), aligned_faces=True),
]

t.explore('example', layouts=layouts, daemon=False)
