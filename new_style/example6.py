#!/usr/bin/env python3

"""
Node style with instructions in dictionaries and decorations.
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout, DEFAULT_LAYOUT, Decoration, TextFace


t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


def node_style(node):
    if node.is_leaf:
        yield {'box': {'fill': 'lightblue'}}
    else:
        yield Decoration(TextFace('I am an inner node'), column=2)


layout = Layout(name='blue leaves', node_style=node_style)

t.explore(layouts=[DEFAULT_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
