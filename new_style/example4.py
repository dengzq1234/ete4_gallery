#!/usr/bin/env python3

"""
Layout using the node_style() function.
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout, DEFAULT_LAYOUT, TextFace


t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


def node_style(node):
    if node.is_leaf:
        return TextFace('I am a leaf!')  # a single return is fine


layout = Layout(name='simple text on leaves', node_style=node_style)

t.explore(layouts=[DEFAULT_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
