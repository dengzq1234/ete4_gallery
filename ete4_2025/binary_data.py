from ete4 import Tree
from ete4.smartview import Layout, RectFace, CircleFace, PolygonFace, TextFace, BASIC_LAYOUT
import random

class TreeLayout:
    def __init__(self, name, shape, rotation, fill_color, stroke_color, column, header, wmax=50, hmax=50, rmax=30):
        self.name = name
        self.shape = shape  # 'square', 'circle', 'triangle'
        self.rotation = rotation
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.column = column
        self.header = header
        self.wmax = wmax
        self.hmax = hmax
        self.rmax = rmax
        self.active = True

    def draw_node(self, node, collapsed=False):
        if node.is_leaf:
            binary_value = node.props.get('binary')
            style = {'fill': self.fill_color if binary_value == 1 else 'none',
                     'stroke': self.stroke_color, 'stroke-width': 1}
            
            if self.shape == 'square':
                yield RectFace(wmax=self.wmax, hmax=self.hmax, style=style, column=self.column, position='aligned')
            elif self.shape == 'circle':
                yield CircleFace(rmax=self.rmax, style=style, column=self.column, position='aligned')
            elif self.shape == 'triangle':
                yield PolygonFace(rmax=self.wmax, shape=3, rotation=self.rotation, style=style, column=self.column, position='aligned')
            
            yield RectFace(wmax=20, hmax=1, style={'fill': 'none'}, column=self.column + 1, position='aligned')
    
    def draw_tree(self, tree):
        yield TextFace(self.header, rotation=-45, position='header', column=self.column)

# Generate a larger random tree
random.seed(42)
tree = Tree()
tree.populate(50, dist_fn=random.random, support_fn=random.random)

# Assign random binary data to leaves, including empty values
for leaf in tree:
    leaf.add_prop('binary', random.choice([0, 1, None]))  # Adding None for empty values

# Define different layouts using TreeLayout
square_layout = TreeLayout('square', 'square', 0, 'blue', 'blue', 1, 'Square')
circle_layout = TreeLayout('circle', 'circle', 0, 'red', 'red', 3, 'Circle')
triangle_left_layout = TreeLayout('triangle_left', 'triangle', 270, 'gold', 'gold', 5, 'Triangle_left')
triangle_right_layout = TreeLayout('triangle_right', 'triangle', 90, 'green', 'green', 7, 'Triangle_right')

# Explore tree with all layouts
tree.explore(layouts=[BASIC_LAYOUT, 
square_layout, 
circle_layout, 
triangle_left_layout, 
triangle_right_layout
])
input()
