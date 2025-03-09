from ete4.smartview.faces import Face
import ete4.smartview.graphics as gr
from ete4.smartview.coordinates import Size, Box, make_box

class SeqMotifFace(Face):
    """A face for visualizing sequence motifs as rounded rectangles with connecting lines."""

    def __init__(self, rects, wmax=500, hmax=50, corner_radius=10, line_color='black', line_width=2,
                 position='aligned', column=0, anchor=None):
        """
        :param rects: List of motif regions, each defined as (start, end, color, label).
        :param wmax: Total width of the sequence visualization.
        :param hmax: Height of the motif boxes.
        :param corner_radius: Radius for rounded corners.
        :param line_color: Color of the connecting lines.
        :param line_width: Width of the connecting lines.
        :param position: Position of the face in the layout.
        :param column: Column index for alignment.
        :param anchor: Alignment anchor.
        """
        super().__init__(position, column, anchor)
        self.rects = rects
        self.wmax = wmax
        self.hmax = hmax
        self.corner_radius = corner_radius
        self.line_color = line_color
        self.line_width = line_width
        self.gaps = self._compute_gaps(rects, wmax)

    def _compute_gaps(self, rects, wmax):
        """Compute the gaps (empty spaces between rectangles)."""
        gaps = []
        prev_end = 0  # Track the last end position

        for start_x, end_x, _, _ in rects:
            if start_x > prev_end:
                gaps.append((prev_end, start_x))  # Store the gap range
            prev_end = end_x  # Update last end

        # Final gap from last rect to wmax
        if prev_end < wmax:
            gaps.append((prev_end, wmax))

        return gaps

    def draw(self, nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
        """Draws motifs as colored rectangles and connecting lines."""
        dx, dy = size
        zx, zy = zoom

        # Compute width and height with respect to zoom
        w = min(zx * dx, self.wmax) if dx > 0 else self.wmax  # Total available width
        h = min(zy * r * dy, self.hmax) if dy > 0 else self.hmax  # Max height

        graphics = []

        # Draw rectangles
        for start_x, end_x, color, label in self.rects:
            rect_width = end_x - start_x

            # Define the actual box for the rectangle
            size = Size(rect_width / zx, h / (r * zy))
            box = make_box((start_x / zx, 0), size)  # Positioning

            # Draw rounded rectangle
            graphics.append(gr.draw_rect(box, {
                'fill': color,
                'opacity': 0.7,
                'stroke': 'black',
                'stroke-width': 2,
                'rx': self.corner_radius,  # Rounded corner in x
                'ry': self.corner_radius   # Rounded corner in y
            }))

            # Add text inside the rectangle
            text_style = {'fill': 'white', 'font-size': '16px', 'text-anchor': 'middle'}
            text_element = gr.draw_text(box, (0.5, 0.5), label, fs_max=16, rotation=0, style=text_style)
            graphics.append(text_element)

        # Draw connecting lines in the gaps
        for gap_start, gap_end in self.gaps:
            if gap_end - gap_start > 0:  # Only draw if the gap is valid
                gap_width = gap_end - gap_start

                # Define the actual box for the line
                size = Size(gap_width / zx, h / (r * zy))
                line_height = h / (r * zy) / 2  # Position line at middle height
                box = make_box((gap_start / zx, line_height), size)  # Positioning at middle height
                style = {'stroke': self.line_color, 'stroke-width': self.line_width}
                graphics.append(
                    gr.draw_line((box.x, box.y), (box.x + box.dx, box.y), style)
                )

        return graphics, Size(w / zx, h / (r * zy))

# Define motif regions
rects = [
    (50, 100, 'blue', 'Domain1'),   # First segment (50-100) → Blue
    (250, 350, 'red', 'Domain2')    # Second segment (250-350) → Red
]

def draw_node(node):
    """Applies SeqMotifFace to leaf nodes."""
    if node.is_leaf:
        yield SeqMotifFace(rects)


# ** Apply Layout & Explore Tree**
from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT

layout = Layout(name='SeqMotifFace', draw_node=draw_node)

t = Tree("(((a1,a2),a3), ((b1,b2),(b3,b4)), ((c1,c2),c3));")

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()