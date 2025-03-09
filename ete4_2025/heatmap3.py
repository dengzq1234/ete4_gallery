import random
from ete4 import Tree
from ete4.smartview import Layout, RectFace, BASIC_LAYOUT

# Create a larger tree with meaningful branch lengths
random.seed(42)  # Ensures reproducibility
t = Tree()
t.populate(30, dist_fn=lambda: random.uniform(0.5, 2.5))  # Branch lengths from ~0.5 to ~2.5

# Function to interpolate colors between blue → white → red
def get_gradient_color(value, min_val=0.5, mid_val=1.5, max_val=2.5):
    """Interpolates RGB color from blue (low), white (mid), to red (high)."""
    if value <= mid_val:
        # Blue (low) to White (mid)
        ratio = (value - min_val) / (mid_val - min_val)
        r, g, b = int(255 * ratio), int(255 * ratio), 255  # Increasing white
    else:
        # White (mid) to Red (high)
        ratio = (value - mid_val) / (max_val - mid_val)
        r, g, b = 255, int(255 * (1 - ratio)), int(255 * (1 - ratio))  # Increasing red
    return f'rgb({r},{g},{b})'  # RGB format

# Function to create a per-node heatmap
def draw_heatmap(node):
    """Generates a heatmap with a smooth gradient based on branch length."""
    if node.is_leaf:
        return [
            RectFace(wmax=30, style={'fill': get_gradient_color(node.dist)}, position='aligned', column=col)
            for col in range(10)  # Fixed 10 columns per node for uniformity
        ]

layout_heatmap = Layout(name="Blue-White-Red Heatmap", draw_node=draw_heatmap)

# Explore tree with the heatmap visualization
t.explore(layouts=[BASIC_LAYOUT, layout_heatmap])
input()
