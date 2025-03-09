from random import random
from ete4 import Tree
from ete4.smartview import Layout, RectFace, BASIC_LAYOUT, TextFace
from ete4.smartview.faces import Face
import ete4.smartview.graphics as gr
from ete4.smartview.coordinates import Size, Box, make_box

class LineFace(Face):
    """A line face with configurable width, optimized like BoxedFace."""
    def __init__(self, wmax, style='', position='top', column=0, anchor=None):
        super().__init__(position, column, anchor)
        self.wmax = wmax  # Maximum width of the line
        self.style = style

    def draw(self, nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
        dx, dy = size
        zx, zy = zoom
        
        # Compute width, ensuring it does not exceed the maximum
        w = min(zx * dx, self.wmax) if dx > 0 else self.wmax
        
        # Define start and end points for the line
        box = make_box((0, 0), Size(w / zx, 0))
        
        # Return the line graphics and its size
        return [gr.draw_line((box.x, box.y), (box.x + box.dx, box.y), self.style)], Size(w / zx, 0)


class BarPlotLayout:
    def __init__(self, name="Branch Length Barplot", fill_color="blue", column=0, width=200, size_range=[0,1]):
        self.name = name
        self.fill_color = fill_color
        self.column = column
        self.width = width
        
        #self.scale = scale
        self.active = True
        self.size_range = [0, 1]

    def get_size(self, node):
        minval, maxval = self.size_range
        return float(node.props.get('dist', 0)) / maxval * self.width

    def draw_node(self, node, collapsed=False):
        if node.is_leaf:
            bar_width = self.get_size(node)
            #yield LineFace(wmax=bar_width, style={'stroke': 'black', 'stroke-width': 2}, position='aligned', column=self.column+1)
            yield RectFace(wmax=bar_width, style={'fill': self.fill_color}, position='aligned', column=self.column)

    def draw_tree(self, tree):
        max_width = self.size_range[1] * self.width
        yield TextFace(self.name, rotation=-90, position='header', column=self.column)
        yield LineFace(wmax=max_width, style={'stroke': 'black', 'stroke-width': 2}, position='header', column=self.column+1)
        
# Create a sample tree with branch lengths assigned
t = Tree()
t.populate(50, dist_fn=lambda: random() )  # Ensures nodes get meaningful distances

# Define the barplot layout
barplot_layout = BarPlotLayout()

# Explore tree with the new barplot layout
t.explore(layouts=[BASIC_LAYOUT, barplot_layout])

input()
