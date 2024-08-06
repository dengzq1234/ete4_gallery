#!/usr/bin/env python3

from random import random

from ete4 import Tree
from ete4.smartview import Layout, DEFAULT_LAYOUT, Decoration, RectFace

t = Tree()
t.populate(20, dist_fn=random, support_fn=random)

def node_decorations(node):
    if node.is_leaf:
        face = RectFace(wmax=80, hmax=70,
                        style={'fill': 'blue'})
        yield Decoration(face, position='aligned')

rects_layout = Layout(name='rects', node_decos=node_decorations)

t.explore(layouts=[DEFAULT_LAYOUT, rects_layout])
input('Tree explorer running. Press enter to stop the server and finish.\n')
