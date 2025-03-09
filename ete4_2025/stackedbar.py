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


random.seed(42)  # so we have the same trees in every run


t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)


def draw_node(node):
    data = [
        ['first', 10, 'red', None],
        ['second', 40, 'blue', None],
        ['green', 50, 'green', None]
    ]
    
    if node.is_leaf:
        face = Face(position='aligned', column=1)
        wmax = 400
        hmax = 40
        opacity = 0.7

        # Override the draw method dynamically
        def draw_fn(nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
            graphics = []  # Store graphics here
            dx, dy = size
            zx, zy = zoom

            # Compute width and height with respect to zoom
            w = min(zx * dx, wmax) if dx > 0 else wmax  # Total available width
            h = min(zy * r * dy, hmax) if dy > 0 else hmax  # Max height

            if len(data) == 1:
                color = data[0][2]
                rect_face = RectFace(
                    wmax=wmax, hmax=hmax,
                    style={'fill': color, 'opacity': opacity},
                    position='aligned',
                    column=1
                )
                rect_graphics, rect_size = rect_face.draw(nodes, size, collapsed, zoom, ax_ay, r)
                graphics.extend(rect_graphics)
            else:
                total_value = sum(d[1] for d in data)  # Total of all segments
                current_x = 0  # Track where to place the next segment
                
                for label, value, color, _ in data:
                    segment_width = (value / total_value) * w  # Proportional width

                    # Define box for the segment
                    size = Size(segment_width / zx, h / (r * zy))
                    box = make_box((current_x / zx, 0), size)  # Positioning

                    # Draw stacked segment
                    graphics.append(gr.draw_rect(box, {
                        'fill': color,
                        'opacity': opacity,
                        'stroke': 'black',
                        'stroke-width': 1
                    }))

                    # Add text inside the segment
                    text_style = {'fill': 'white', 'font-size': '12px', 'text-anchor': 'middle'}
                    text_element = gr.draw_text(box, (0.5, 0.5), label, fs_max=12, rotation=0, style=text_style)
                    graphics.append(text_element)

                    current_x += segment_width  # Move position for next segment

            return graphics, Size(w / zx, h / (r * zy))

        # Assign the dynamic draw function
        face.draw = draw_fn

        yield face
        


layout = Layout(name='Stacked Bar', draw_node=draw_node)

# layout = Layout(name='rects', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
