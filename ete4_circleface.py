#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, CircleFace
import random

t = Tree()
t.populate(20, random_branches=True)

# List of colors
colors = ['red', 'blue', 'green']

def get_face(node):
    if node.is_leaf:
        random_number = random.randint(2, 20)
        selected_color = random.choice(colors)
        face = CircleFace(
            radius=random_number, color=selected_color, name="circle_face",
            padding_x=2, padding_y=2, tooltip=None)
        node.add_face(face, position='aligned', column=1)
    return


layouts = [
    TreeLayout(name='circle', ns=get_face, aligned_faces=True),
]

t.explore(layouts=layouts, keep_server=True)
