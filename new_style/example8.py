#!/usr/bin/env python3

"""
Tree style and node style with many options.
"""

from random import random

from ete4 import Tree
from ete4.smartview import (Layout, BASIC_LAYOUT, Decoration, BoxFace,
                            PropFace, TextFace)


t = Tree()
t.populate(50, dist_fn=random, support_fn=random)

for node in t.traverse():
    node.props['coolness'] = random()


def too_deep(node):
    return node.level > 5


tree_style = {
    'shape': 'circular',
    'limits': (2, 0, -90, 90),
    'is-leaf-fn': too_deep,
    'min-size': 15,
    'dot': {'shape': 'none'}, # {'radius': 10, 'fill': 'green'},
    'hz-line': {'stroke': 'red', 'stroke-width': 5},
    'vt-line': {'stroke': '#ffff00', 'stroke-width': 3},
    'box': {'fill': '#e0e0e0'},
    'aliases': {
        'support': {'fill': 'green'},  # used in default layout's support
        'myblue': {'fill': 'blue', 'font-weight': 'bold'},
    }
}


def draw_node(node, collapsed):
    yield Decoration(TextFace('visited node'), position='bottom')

    yield Decoration(PropFace('coolness', fmt='%.2g',
                              style='myblue'),
                     position='bottom', column=1, anchor=(1, -1))

    if node.is_leaf:
        yield {'box': {'border': '4px',
                       'stroke': 'blue',
                       'fill': 'green'},
               'dot': {'fill': 'red',
                       'shape': 'hexagon',
                       'stroke': 'yellow',
                       'opacity': 1,
                       'radius': 20},
               'hz-line': {'stroke-width': 2}}
        face = BoxFace(wmax=80, hmax=70,
                       style={'fill': 'lightblue'},
                       text=f'node at depth {node.level}')
        yield Decoration(face, position='aligned')
    elif collapsed:
        face = BoxFace(wmax=80, hmax=70,
                       style={'fill': 'red'},
                       text='Collapsing nodes')
        yield Decoration(face, position='aligned')


layout = Layout(name='many',
                draw_tree=tree_style,
                draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
