#!/usr/bin/env python3

from random import random, randint, choice
from functools import cache

from ete4 import Tree
from ete4.smartview import Layout, DEFAULT_LAYOUT, Decoration, CircleFace

t = Tree()
t.populate(20, dist_fn=random, support_fn=random)

colors = ['red', 'blue', 'green']  # color to choose from

@cache
def node_decorations(node):
    if node.is_leaf:
        face = CircleFace(rmax=randint(2, 20),
                          style={'fill': choice(colors)})
        return Decoration(face, position='aligned')

circles_layout = Layout(name='circles', node_decos=node_decorations)

t.explore(layouts=[DEFAULT_LAYOUT, circles_layout])
input('Tree explorer running. Press enter to stop the server and finish.')
