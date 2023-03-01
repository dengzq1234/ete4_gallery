#!/usr/bin/env python3

import os

from ete4 import Tree
from ete4.smartview import TreeLayout, ImgFace


TREEFILE = 'basic_example1_annotated.nw'
ABSOLUTE_IMGPATH = os.path.abspath('frog.jpeg')

popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2', 'sample3', 'sample4', 'sample5',
    'random_type', 'bool_type', 'bool_type2'
]

t = Tree(TREEFILE, format=1)
level = 2  # level 1 is leaf name


def get_face(prop):
    def layout_fn(node):
        if node.is_leaf():
            face = ImgFace(
                img_path=ABSOLUTE_IMGPATH, width=70, height=50, name='',
                padding_x=0, padding_y=0)
            node.add_face(face, position='aligned', column=level)

    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face('sample1'), aligned_faces=True),
]

t.explore(tree_name='example', layouts=layouts, popup_prop_keys=popup_prop_keys)
