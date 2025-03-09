from ete4.smartview import Layout, BASIC_LAYOUT
from ete4 import Tree

class BranchStyleLayout(Layout):
    """Defines a layout for branch lines with customizable styles."""

    def __init__(self, name="Branch Style Layout",
                 hz_color="black", hz_width=2, hz_dash=None, hz_opacity=1.0,
                 vt_color="black", vt_width=2, vt_dash=None, vt_opacity=1.0,
                 collapsed_hz_color="gray", collapsed_vt_color="gray"):
        """
        Initializes a layout with specific branch styles.

        :param name: Name of the layout.
        :param hz_color: Color for horizontal lines.
        :param hz_width: Width of horizontal lines.
        :param hz_dash: Dashed pattern for horizontal lines (e.g., "5,5").
        :param hz_opacity: Opacity of horizontal lines (0.0 - 1.0).
        :param vt_color: Color for vertical lines.
        :param vt_width: Width of vertical lines.
        :param vt_dash: Dashed pattern for vertical lines (e.g., "5,5").
        :param vt_opacity: Opacity of vertical lines (0.0 - 1.0).
        :param collapsed_hz_color: Horizontal line color for collapsed nodes.
        :param collapsed_vt_color: Vertical line color for collapsed nodes.
        """
        self.hz_style = {
            "stroke": hz_color,
            "stroke-width": hz_width,
            "stroke-opacity": hz_opacity,
        }
        if hz_dash:
            self.hz_style["stroke-dasharray"] = hz_dash

        self.vt_style = {
            "stroke": vt_color,
            "stroke-width": vt_width,
            "stroke-opacity": vt_opacity,
        }
        if vt_dash:
            self.vt_style["stroke-dasharray"] = vt_dash

        # Collapsed branch styles
        self.collapsed_hz_style = {"stroke": collapsed_hz_color}
        self.collapsed_vt_style = {"stroke": collapsed_vt_color}

        # Initialize parent Layout class
        super().__init__(name=name, draw_node=self.draw_node, active=True)

    def draw_node(self, node, collapsed=False):
        """Applies the branch line styles."""
        if collapsed:
            yield {"hz-line": self.collapsed_hz_style, "vt-line": self.collapsed_vt_style}
        yield {"hz-line": self.hz_style, "vt-line": self.vt_style}

# Define different branch styles
dashed_layout = BranchStyleLayout("Dashed Branches", hz_dash="5,5", vt_dash="3,3", hz_color="red", vt_color="blue")
thick_layout = BranchStyleLayout("Thick Branches", hz_width=5, vt_width=5, hz_color="green", vt_color="purple")
faint_layout = BranchStyleLayout("Faint Branches", hz_opacity=0.3, hz_width=7, vt_opacity=0.3, hz_color="brown", vt_color="red")

# Generate a test tree
t = Tree("(((a,b),c),d);")

# Apply layouts
t.explore(layouts=[BASIC_LAYOUT, dashed_layout, thick_layout, faint_layout])
input()
