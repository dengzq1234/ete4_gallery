#!/usr/bin/env python3

import os

from ete4 import Tree
from ete4.smartview import TreeLayout, ImgFace

ABSOLUTE_IMGPATH = os.path.abspath('example_data/frog.jpeg')

t = Tree()
t.populate(20, random_branches=True)





def get_face(node):
    if node.is_leaf:
        face = ImgFace(
            img_path=ABSOLUTE_IMGPATH, width=70, height=50, name='',
            padding_x=0, padding_y=0)
        node.add_face(face, position='aligned')

    return


layouts = [
    TreeLayout(name='sample1', ns=get_face, aligned_faces=True),
]

t.explore(layouts=layouts, keep_server=True)

