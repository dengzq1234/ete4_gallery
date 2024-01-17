#!/usr/bin/env python3

import random

from ete4 import Tree
from ete4.smartview import TreeLayout, ArrowFace

t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)

# List of directions
directions = ['left', 'right']
colors = ['red', 'blue', 'green']

def layout_arrow(node):
    if node.is_leaf:
        random_direction = random.choice(directions)
        selected_color = random.choice(colors)

        arrow_face = ArrowFace(
            width=100, height=70, orientation=random_direction,
            color=selected_color, stroke_color='gray', stroke_width='1.5px',
            text=None, fgcolor='black',
            min_fsize=6, max_fsize=15,
            ftype='sans-serif',
            name=f'I am thee arrow of node {node.name}!',
            padding_x=0, padding_y=0,
            tooltip=None)

        node.add_face(arrow_face, position='aligned')

layouts = [
    TreeLayout(name='sample1', ns=layout_arrow, aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
