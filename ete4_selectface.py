#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, SelectedCircleFace, SelectedRectFace


TREEFILE = 'example_data/tree.nw'

popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2', 'sample3', 'sample4', 'sample5',
    'random_type', 'bool_type', 'bool_type2'
]

t = Tree(TREEFILE, format=1)
level = 2  # level 1 is leaf name

def get_face(prop):
    def layout_fn(node):
        if not node.is_leaf():
            return

        node_val = float(node.props.get(prop))
        if node_val > 0.50:
            face = SelectedCircleFace(prop, radius=20,
                                      padding_x=2, padding_y=2)
        else:
            face = SelectedRectFace(prop, width=15, height=15,
                                    padding_x=2, padding_y=2)
        node.add_face(face, position='aligned', column=level)

    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face('sample1'), aligned_faces=True),
]

t.explore(tree_name='example', layouts=layouts, popup_prop_keys=popup_prop_keys)
