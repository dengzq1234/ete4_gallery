#!/usr/bin/env python3

"""
Use of node_style(node, collapsed), and is_leaf_fn().
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout, DEFAULT_LAYOUT, Decoration, BoxFace, TextFace


t = Tree()
t.populate(30, dist_fn=random, support_fn=random)


tree_style = {
    'box': {'fill': 'blue', 'opacity': 0.1},
    'aliases': {
        'leaf': {'fill': 'green', 'stroke': 'green', 'opacity': 1},
    }
}


def node_style(node, collapsed):
    if node.is_leaf:
        yield {'box': 'leaf',
               'dot': {'fill': 'red'}}
        yield TextFace('I am a leaf', style={'fill': 'white',
                                             'stroke': 'black',
                                             'stroke-width': 0.5})

    if collapsed:
        ndesc = sum(1 for sibling in collapsed for n in sibling.traverse())
        face = BoxFace(wmax=80, hmax=70,
                       style={'fill': 'red'},
                       text=f'I have {ndesc} descendants')
        yield Decoration(face, position='aligned')


rects_layout = Layout(name='rects',
                      tree_style=tree_style,
                      node_style=node_style)


def too_deep(node):
    return node.level > 4

t.explore(layouts=[DEFAULT_LAYOUT, rects_layout], is_leaf_fn=too_deep)

print('Press enter to stop the server and finish.')
input()
