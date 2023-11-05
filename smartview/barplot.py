#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, RectFace, TextFace, ScaleFace
import random

t = Tree()
t.populate(20, random_branches=True)

# annotate numerical values to each leaf
for node in t.leaves():
    node.add_prop('count', random.randint(1, 100))

# define tree style function
def layout_tree_style(tree_style):
    # add scale bar to footer
    scaleface = ScaleFace(
        name='sample1', 
        width=150, 
        color='black',
        scale_range=(0, 100), 
        tick_width=80, 
        line_width=1,
        formatter='%.0f',
        min_fsize=6, 
        max_fsize=12, 
        ftype='sans-serif',
        padding_x=0, 
        padding_y=0)

    tree_style.aligned_panel_header.add_face(scaleface, column=0)
    tree_style.aligned_panel_footer.add_face(scaleface, column=0)

    # add title to header and footer
    text = TextFace("Count", min_fsize=5, max_fsize=12, width=50, rotation=0)
    tree_style.aligned_panel_header.add_face(text, column=0)    
    return 

# define node Face layout function
def layout_barplot(node):
    if node.is_leaf:
        width = node.props.get('count') * 1.5
        rect_face = RectFace(
            width=width, height=70, color='skyblue',
            opacity=0.7, text=None, fgcolor='black',
            min_fsize=6, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0,
            tooltip=None)
        node.add_face(rect_face, position='aligned', column=0)
        return 

# Create a TreeLayout object, passing in the function
barplot_layout = TreeLayout(
    name='BarPlot',
    ns=layout_barplot, 
    ts=layout_tree_style,
    aligned_faces=True)

# add layout to layouts list
layouts = []
layouts.append(barplot_layout)
t.explore(
    layouts=layouts, 
    include_props=("name", "dist", "length"),
    keep_server=True)
