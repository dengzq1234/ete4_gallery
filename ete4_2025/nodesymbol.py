from ete4.smartview import Layout, BASIC_LAYOUT
from ete4 import Tree

class NodeShapeLayout(Layout):
    """Defines a layout for node symbols with customizable shapes and styles."""

    def __init__(self, name="Node Shape Layout", shape="circle", radius=5, 
                 fill="black", opacity=1.0, stroke="black", stroke_width=1,
                 stroke_dasharray=None, rotation=0, collapsed_shape=None, collapsed_fill="gray"):
        """
        Initializes a layout with a specific node shape and styles.

        :param name: Name of the layout.
        :param shape: Node shape ('circle', 'square', 'triangle', 'pentagon', 'hexagon', 'star', etc.).
        :param radius: Approximate radius/size in pixels.
        :param fill: Fill color of the shape.
        :param opacity: Opacity of the shape (0.0 - 1.0).
        :param stroke: Stroke (border) color.
        :param stroke_width: Stroke width in pixels.
        :param stroke_dasharray: Dash pattern for stroke (e.g., "5,5" for dashed lines).
        :param collapsed_shape: Shape to use when the node is collapsed (default is same as shape).
        :param collapsed_fill: Fill color when the node is collapsed.
        """
        self.shape = shape
        self.radius = radius
        self.fill = fill
        self.opacity = opacity
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.stroke_dasharray = stroke_dasharray
        self.rotation = rotation
        self.collapsed_shape = collapsed_shape or shape
        self.collapsed_fill = collapsed_fill

        # Initialize parent Layout class
        super().__init__(name=name, draw_node=self.draw_node, active=True)

    def draw_node(self, node, collapsed=False):
        """Applies the shape style to nodes, supporting collapsed node representation."""
        style = {
            "shape": self.collapsed_shape if collapsed else self.shape,
            "radius": self.radius,
            "fill": self.collapsed_fill if collapsed else self.fill,
            "opacity": self.opacity,
            "stroke": self.stroke,
            "stroke-width": self.stroke_width,
            "rotation": self.rotation
        }
        
        if self.stroke_dasharray:
            style["stroke-dasharray"] = self.stroke_dasharray  # Optional dashed lines

        yield {"dot": style}

# Define different node styles
circle_layout = NodeShapeLayout("Circle Nodes", shape="circle", radius=8, fill="red", opacity=0.8)
square_layout = NodeShapeLayout("Square Nodes", shape="square", radius=10, fill="blue", stroke="black", stroke_width=2)
triangle_layout = NodeShapeLayout("Triangle Nodes", shape="triangle", radius=10, fill="green", stroke="black", stroke_dasharray="5,5", rotation=90)
pentagon_layout = NodeShapeLayout("Pentagon Nodes", shape=5, radius=12, fill="purple", stroke="black", stroke_width=3)
hexagon_layout = NodeShapeLayout("Hexagon Nodes", shape=6, radius=12, fill="orange", stroke="black", stroke_width=2)

# Generate a test tree
t = Tree("(((a,b),c),d);")

# Apply layouts
t.explore(layouts=[BASIC_LAYOUT, circle_layout, square_layout, triangle_layout, pentagon_layout, hexagon_layout])

input()