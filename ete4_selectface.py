#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, SelectedCircleFace, SelectedRectFace


TREEFILE = 'example_data/tree.nw'

t = Tree(open(TREEFILE))


def get_face(prop):
    def layout_fn(node):
        if not node.is_leaf:
            return

        node_val = float(node.props.get(prop))
        if node_val > 0.50:
            face = SelectedCircleFace(prop, radius=20,
                                      padding_x=2, padding_y=2)
        else:
            face = SelectedRectFace(prop, width=15, height=15,
                                    padding_x=2, padding_y=2)
        node.add_face(face, position='aligned')

    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face('sample1'), aligned_faces=True),
]

t.explore('example', layouts=layouts)
