from ete4 import Tree
from ete4.smartview import Layout, RectFace, CircleFace, PolygonFace, TextFace, BASIC_LAYOUT
import random
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

# Example usage
random.seed(42)
tree = Tree()
tree.populate(10, dist_fn=lambda: random.random() * 2)

def draw_node(node):
    if node.is_leaf:
        yield LineFace(wmax=500, style={'stroke': 'black', 'stroke-width': 2}, position='aligned')

line_layout = Layout(name='Line Layout', draw_node=draw_node)

# Explore tree with the new line layout
tree.explore(layouts=[BASIC_LAYOUT, line_layout])

input()

