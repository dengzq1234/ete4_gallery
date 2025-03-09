import random
from ete4.smartview import Layout, BASIC_LAYOUT
from ete4 import Tree

class BoxStyleLayout(Layout):
    """Defines a layout for node boxes with customizable styles."""

    def __init__(self, name="Box Style Layout",
                 fill="white", stroke="black", stroke_width=2, opacity=1.0, rounded=False):
        """
        Initializes a layout with specific box styles.

        :param name: Name of the layout.
        :param fill: Fill color of the box.
        :param stroke: Stroke (border) color of the box.
        :param stroke_width: Width of the box border.
        :param opacity: Opacity of the box (0.0 - 1.0).
        :param rounded: Whether to apply rounded corners.
        """
        self.box_style = {
            "fill": fill,
            "stroke": stroke,
            "stroke-width": stroke_width,
            "opacity": opacity
        }
        if rounded:
            self.box_style["rx"] = 10  # Rounded corners

        # Initialize parent Layout class
        super().__init__(name=name, draw_node=self.draw_node, active=True)

    def draw_node(self, node, collapsed=False):
        """Applies the box style to nodes."""
        yield {"box": self.box_style}

# Define different box styles
red_box_layout = BoxStyleLayout("Red Boxes", fill="red", stroke="black", stroke_width=3, opacity=0.8)
blue_box_layout = BoxStyleLayout("Blue Boxes", fill="blue", stroke="yellow", stroke_width=2, opacity=0.6, rounded=True)
transparent_box_layout = BoxStyleLayout("Transparent Boxes", fill="none", stroke="gray", stroke_width=1, opacity=0.4)

# Generate a larger tree
random.seed(42)  # Ensures reproducibility
t = Tree()
t.populate(50, dist_fn=random.random, support_fn=random.random)

# Apply layouts
t.explore(layouts=[BASIC_LAYOUT, red_box_layout, blue_box_layout, transparent_box_layout])
input()
