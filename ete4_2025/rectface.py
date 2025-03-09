#!/usr/bin/env python3

"""
Example of use of RectFace.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, RectFace

from ete4.smartview.faces import Face
import ete4.smartview.graphics as gr
from ete4.smartview.coordinates import Size, Box, make_box

# class LineFace(Face):
#     """A line face with configurable width, optimized like BoxedFace."""
#     def __init__(self, wmax, style='', position='top', column=0, anchor=None):
#         super().__init__(position, column, anchor)
#         self.wmax = wmax  # Maximum width of the line
#         self.style = style

#     def draw(self, nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
#         dx, dy = size
#         zx, zy = zoom

#         # Compute width, ensuring it does not exceed the maximum
#         w = min(zx * dx, self.wmax) if dx > 0 else self.wmax
        
#         # Define start and end points for the line
#         box = make_box((0, 0), Size(w / zx, 0))
        
#         # Return the line graphics and its size
#         return [gr.draw_line((box.x, box.y), (box.x + box.dx, box.y), self.style)], Size(w / zx, 0)

# Example usage

random.seed(42)  # so we have the same trees in every run


t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)

# def draw_node(node):
#     if node.is_leaf:
#         column = 1
#         yield RectFace(wmax=80, hmax=70,
#                        style={'fill': 'blue', 'opacity': 0.7},
#                        position='aligned',
#                        column=column)  # some will superimpose
                       
#         #yield LineFace(wmax=80, style={'stroke': 'black', 'stroke-width': 2}, position='aligned', column=column+2)


def draw_node(node):
    if node.is_leaf:
        
        yield RectFace(
            wmax=80, hmax=70,
            style={'fill': 'blue', 'opacity': 0.7},  # Tooltip!
            position='aligned',
            column=1
        )

layout = Layout(name='Rectangles with Tooltips', draw_node=draw_node)

# layout = Layout(name='rects', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
