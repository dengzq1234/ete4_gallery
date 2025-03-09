from random import random
from ete4 import Tree
from ete4.smartview import Layout, RectFace, BASIC_LAYOUT

# Create a tree with meaningful branch lengths
t = Tree()
t.populate(10, dist_fn=lambda: random() * 2)  # Branch lengths from 0 to ~2

# Function to map a column index to a gradient color
def get_column_color(value, col, total_cols=100):
    """Maps a column index within a value range to a smooth color gradient."""
    mid_col = total_cols // 2
    if col <= mid_col:
        # Blue → White (left half of the gradient)
        ratio = col / mid_col
        r, g, b = int(255 * ratio), int(255 * ratio), 255  # More white, keeping blue
    else:
        # White → Red (right half of the gradient)
        ratio = (col - mid_col) / (total_cols - mid_col)
        r, g, b = 255, int(255 * (1 - ratio)), int(255 * (1 - ratio))  # More red, reducing white
    return f'rgb({r},{g},{b})'  # RGB format

### **🌡️ Heatmap Layout (100 Columns)**
def draw_heatmap(node):
    """Generates 100 heatmap bars, transitioning color smoothly across the columns."""
    if node.is_leaf:
        return [
            RectFace(wmax=60, style={'fill': get_column_color(node.dist, col)}, position='aligned', column=col)
            for col in range(1000)
        ]

layout_heatmap = Layout(name="Smooth Column Gradient Heatmap (100 Columns)", draw_node=draw_heatmap)

# Explore tree with the heatmap visualization
t.explore(layouts=[BASIC_LAYOUT, layout_heatmap])
input()