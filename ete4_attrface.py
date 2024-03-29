#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout
from ete4.smartview  import AttrFace


TREEFILE = 'example_data/tree.nw'

t = Tree(open(TREEFILE))


def get_attrface(prop):
    def layout_fn(node):
        if not node.is_leaf:
            return

        attr_face = AttrFace(
            prop,
            name='sample1',
            color='red',
            min_fsize=6, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0)

        node.add_face(attr_face, position='aligned')

    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_attrface('sample1'), aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
