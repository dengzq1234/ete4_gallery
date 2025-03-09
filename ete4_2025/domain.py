from random import random
from ete4 import Tree
from ete4.smartview import Layout, RectFace, BASIC_LAYOUT, TextFace
from ete4.smartview.faces import Face
import ete4.smartview.graphics as gr
from ete4.smartview.coordinates import Size, Box, make_box


class SeqMotifFace(Face):
    """A face for visualizing sequence motifs as colored rectangles with text."""

    def __init__(self, motifs, wmax=400, hmax=30, position="aligned", column=0, anchor=None):
        """
        :param motifs: List of motif annotations, each containing:
            [start, end, '()', None, None, fill_color, border_color, font_style]
            - start, end: Position of motif in sequence.
            - fill_color, border_color: Motif colors.
            - font_style: "font|size|color|text" (e.g., "arial|30|black|P53").
        :param wmax: Maximum width of the motif sequence visualization.
        :param hmax: Maximum height of the motif boxes.
        :param position: Position of the face in the layout.
        :param column: Column index for alignment.
        :param anchor: Alignment anchor.
        """
        super().__init__(position, column, anchor)
        self.motifs = motifs
        self.wmax = wmax  # Max width of sequence motifs
        self.hmax = hmax  # Max height of motifs

    def draw(self, nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
        """
        Draws motifs as colored rectangles within the bounding box.
        """
        if not self.motifs:
            return [], Size(0, 0)  # No motifs, nothing to draw

        dx, dy = size
        zx, zy = zoom

        # **Step 1**: Compute bounding box width and height based on zoom
        w = min(zx * dx, self.wmax) if dx > 0 else self.wmax
        h = min(zy * r * dy, self.hmax) if self.hmax else (zy * r * dy)

        # Maintain aspect ratio
        if self.hmax:
            h_over_w = self.hmax / self.wmax
            if h / w > h_over_w:
                h = h_over_w * w
            else:
                w = h / h_over_w

        # Define bounding box
        bounding_size = Size(w / zx, h / (r * zy))
        bounding_box = make_box((0, 0), bounding_size)

        # **Step 2**: Compute motif positions dynamically
        seq_start = min(m[0] for m in self.motifs)
        seq_end = max(m[1] for m in self.motifs)
        seq_length = seq_end - seq_start

        # Compute scaling factor (maps motif positions to adjusted width)
        scale = w / seq_length

        # Set up graphics container
        graphics = [gr.draw_rect(bounding_box, {"fill": "none", "stroke": "black"})]  # Visualize bounding box
        prev_end = seq_start  # Track last drawn position

        for motif in self.motifs:
            start, end, shape = motif[:3]
            fill_color, border_color = motif[5:7]
            font_info = motif[7].split("|") if motif[7] else ["arial", "20", "black", ""]

            # Compute motif box width and position
            motif_width = (end - start) * scale
            box_x = (start - seq_start) * scale

            # Draw motif rectangle (rounded if shape == "()")
            rect_style = {"fill": fill_color, "stroke": border_color, "stroke-width": 2}
            motif_box = make_box((box_x, 0), Size(motif_width, h))
            graphics.append(gr.draw_rect(motif_box, rect_style))

            # Add motif label (text inside the box)
            font_name, font_size, font_color, text = font_info
            if text:
                text_face = TextFace(text, fs_max=int(font_size), rotation=0, style={"fill": font_color})
                text_graphics, _ = text_face.draw(nodes, bounding_size, collapsed, zoom, (0.5, 0.5), r)
                graphics.extend(text_graphics)  # Extract raw SVG elements

            prev_end = end  # Update last drawn position

        return graphics, bounding_size



# Define example motifs
motifs = [
    [100, 200, '()', None, None, 'red', 'red', 'arial|20|black|P53'],
    [300, 400, '[]', None, None, 'blue', 'blue', 'arial|20|black|P53_tetramer']
]

# # Create the motif face
# motif_face = SeqMotifFace(motifs, wmax=500, hmax=40)

# # Define layout
# def draw_node(node):
#     """Applies the motif face to leaf nodes."""
#     if node.is_leaf:
#         yield motif_face

#layout = Layout(name="Sequence Motifs", draw_node=draw_node)

# ** Define Tree Layout**
def draw_node(node):
    """Applies Face to leaf nodes without defining a subclass."""
    if node.is_leaf:
        face = Face(position='aligned', column=1)
        wmax = 500
        hmax = 50
        corner_radius = 10  # Radius for rounded corners
        line_color = 'black'  # Line color
        line_width = 2  # Line thickness

        # Define the two rectangles' positions and sizes
        rects = [
            (50, 100, 'blue', 'Domain1'),   # First segment (50-100) → Blue
            (250, 350, 'red', 'Domain2')    # Second segment (250-350) → Red
        ]

        # Calculate the gaps (empty spaces between rectangles)
        gaps = []
        prev_end = 0  # Track the last end position

        for start_x, end_x, _, _ in rects:
            if start_x > prev_end:
                gaps.append((prev_end, start_x))  # Store the gap range
            prev_end = end_x  # Update last end

        # Final gap from last rect to wmax
        if prev_end < wmax:
            gaps.append((prev_end, wmax))

        # Override the draw method dynamically
        def draw_fn(nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
            dx, dy = size
            zx, zy = zoom

            # Compute width and height with respect to zoom
            w = min(zx * dx, wmax) if dx > 0 else wmax  # Total available width
            h = min(zy * r * dy, hmax) if dy > 0 else hmax  # Max height

            graphics = []

            # Draw rectangles
            for start_x, end_x, color, label in rects:
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
                    'rx': corner_radius,  # Rounded corner in x
                    'ry': corner_radius   # Rounded corner in y
                }))

                # Add text inside the rectangle
                text_style = {'fill': 'white', 'font-size': '16px', 'text-anchor': 'middle'}
                text_element = gr.draw_text(box, (0.5, 0.5), label, fs_max=16, rotation=0, style=text_style)
                
                graphics.append(text_element)

            # Draw connecting lines in the gaps
            for gap_start, gap_end in gaps:
                if gap_end - gap_start > 0:  # Only draw if the gap is valid
    
                    # Compute the width of the gap (ensuring it does not exceed wmax)
                    gap_width = gap_end - gap_start

                    # Define the actual box for the line
                    size = Size(gap_width / zx, h / (r * zy))
                    line_height = h / (r * zy)/2 # position line at middle height
                    box = make_box((gap_start / zx, line_height), size)  # Positioning at middle height
                    style = {'stroke': line_color, 'stroke-width': line_width}
                    graphics.append(
                        gr.draw_line((box.x, box.y), (box.x + box.dx, box.y), style)
                    )

            return graphics, Size(w / zx, h / (r * zy))

        # Assign the dynamic draw function
        face.draw = draw_fn

        yield face


# ** Apply Layout & Explore Tree**
from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT

layout = Layout(name='Rectangles with Tooltips', draw_node=draw_node)

t = Tree("(((a1,a2),a3), ((b1,b2),(b3,b4)), ((c1,c2),c3));")

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()