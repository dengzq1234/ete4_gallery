from ete4 import Tree
from ete4.smartview import Layout, TextFace, RectFace, BASIC_LAYOUT
from ete4.smartview.faces import Face, BoxedFace, BoxFace

import ete4.smartview.graphics as gr
from ete4.smartview.coordinates import Size, Box, make_box

# class RotatedTextRectFace(Face):
#     """A rectangle face that allows text inside to be rotated."""
    
#     def __init__(self, wmax, hmax=None, text="", rotation=0, style='',
#                  font_size=12, text_fill="black", position='top', column=0, anchor=None):
#         """
#         :param wmax: Maximum width of the rectangle.
#         :param hmax: Maximum height of the rectangle.
#         :param text: Text to display inside the rectangle.
#         :param rotation: Rotation angle (in degrees) of the text.
#         :param style: Dictionary of styling options for the rectangle.
#         :param font_size: Font size for the text.
#         :param text_fill: Color of the text.
#         :param position: Position of the face (aligned, header, etc.).
#         :param column: Column position for alignment.
#         :param anchor: Anchor point (controls positioning).
#         """
#         super().__init__(position, column, anchor)
        
#         self.wmax = wmax
#         self.hmax = hmax
#         self.text = text
#         self.rotation = rotation
#         self.style = style
#         self.font_size = font_size  # Custom font size
#         self.text_fill = text_fill  # Text color

#     def draw(self, nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
#         """
#         Draws a rectangle with rotated text inside.
#         """
#         dx, dy = size
#         zx, zy = zoom

#         # Compute dimensions (constrained by max size)
#         w = min(zx * dx, self.wmax) if dx > 0 else self.wmax
#         h = min(zy * r * dy, self.hmax) if self.hmax else (zy * r * dy)

#         # Ensure aspect ratio
#         if self.hmax:
#             h_over_w = self.hmax / self.wmax
#             if h / w > h_over_w:
#                 h = h_over_w * w
#             else:
#                 w = h / h_over_w

#         # Create rectangle box
#         size = Size(w/zx, h/(r*zy))
#         box = make_box((0, 0), size)
#         graphics = [gr.draw_rect(box, self.style)]

#         # Add rotated text
#         if self.text:
#             text_element = gr.draw_text(
#                 box, (0.5, 0.5), self.text,
#                 fs_max=self.font_size, rotation=self.rotation,
#                 style={'fill': self.text_fill}
#             )
#             graphics.append(text_element)

#         return graphics, size

class RotatedTextRectFace(BoxedFace):
    """A rectangle face that allows text inside to be rotated."""

    def __init__(self, wmax, hmax=None, text="", rotation=0, style='',
                 font_size=12, text_fill="black", position='top', column=0, anchor=None):
        """
        :param wmax: Maximum width of the rectangle.
        :param hmax: Maximum height of the rectangle.
        :param text: Text to display inside the rectangle.
        :param rotation: Rotation angle (in degrees) of the text.
        :param style: Dictionary of styling options for the rectangle.
        :param font_size: Font size for the text.
        :param text_fill: Color of the text.
        :param position: Position of the face (aligned, header, etc.).
        :param column: Column position for alignment.
        :param anchor: Anchor point (controls positioning).
        """
        super().__init__(wmax, hmax, text, position, column, anchor)

        self.style = style
        self.font_size = font_size  # Custom font size
        self.text_fill = text_fill  # Text color
        self.rotation = rotation
        self.text = TextFace(text, rotation=self.rotation) if type(text) is str else text
        
        # Set the drawing function from BoxedFace
        self.drawing_fn = lambda box: gr.draw_box(box, self.style)

    def draw(self, nodes, size, collapsed, zoom=(1, 1), ax_ay=(0, 0), r=1):
        """
        Draws a rotated rectangle with text inside.
        """
        graphics, size = super().draw(nodes, size, collapsed, zoom, ax_ay, r)
        
        if self.text:
            #self.text.rotation = self.rotation
            # Draw the text centered in x (0.5). But we have to shift the y
            # "by hand" because faces let the caller anchor in y afterwards
            # (so several faces can be vertically stacked and then anchored).
            graphics_text, size_text = self.text.draw(nodes, size, collapsed,
                                                      zoom, (0.5, 0.5), r)
            circular = False
            shift = (0, (size.dy - size_text.dy) / 2)  # shift the y
            graphics += gr.draw_group(graphics_text, circular, shift)

        return graphics, size

t = Tree('((((a1,a2),a3), ((b1,b2),(b3,b4))), ((c1,c2),c3));')

# Define colors for each common ancestor.
style1 = {'fill': 'LightSteelBlue'}
style2 = {'fill': 'Moccasin'}
style3 = {'fill': 'DarkSeaGreen'}
style4 = {'fill': 'Khaki'}

# Find common ancestors.
n1 = t.common_ancestor(['a1', 'a2', 'a3'])
n2 = t.common_ancestor(['b1', 'b2', 'b3', 'b4'])
n3 = t.common_ancestor(['c1', 'c2', 'c3'])
n4 = t.common_ancestor(['b3', 'b4'])

# # Define custom node style
def draw_node(node):
    """Assigns a colored rotated rectangle to common ancestors."""
    if node == n1:
        yield RotatedTextRectFace(
            wmax=120, text="Group A", rotation=90, font_size=120, 
            text_fill="black", position="aligned", style={'fill': 'LightSteelBlue'}
        )
    elif node == n2:
        yield RotatedTextRectFace(
            wmax=120, text="Group B", rotation=90, font_size=120, 
            text_fill="darkred", position="aligned", style={'fill': 'Moccasin'}
        )
    elif node == n3:
        yield RotatedTextRectFace(
            wmax=120, text="Group C", rotation=90, font_size=120, 
            text_fill="white", position="aligned", style={'fill': 'DarkSeaGreen'}
        )
    elif node == n4:
        yield RotatedTextRectFace(
            wmax=120, text="Group D", rotation=90, font_size=120, 
            text_fill="navy", position="aligned", style={'fill': 'Khaki'}
        )
# Define custom node style

# def draw_node(node):
#     """Assigns a colored box with text to common ancestors."""
#     if node == n1:
#         yield BoxFace(wmax=80, 
#                       style={'fill': 'LightSteelBlue'},
#                       text=f'node at depth {node.level}',
#                       position='aligned')
#     elif node == n2:
#         yield BoxFace(wmax=80, 
#                       style={'fill': 'Moccasin'},
#                       text="Group B",
#                       position='aligned')
#     elif node == n3:
#         yield BoxFace(wmax=80, 
#                       style={'fill': 'DarkSeaGreen'},
#                       text="Group C",
#                       position='aligned')
#     elif node == n4:
#         yield BoxFace(wmax=80, 
#                       style={'fill': 'Khaki'},
#                       text="Group D",
#                       position='aligned')


layout = Layout('Rotated Rectangles', draw_node=draw_node)
t.explore(layouts=[BASIC_LAYOUT, layout])
input()
