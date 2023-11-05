#!/usr/bin/env python3

import matplotlib as mpl
import numpy as np

from ete4 import Tree
from ete4.smartview import TreeLayout, RectFace, TextFace
import random


t = Tree()
t.populate(20, random_branches=True)

# annotate numerical values to each leaf
for node in t.leaves():
    node.add_prop('frequence', random.random())

# define tree style function
def layout_tree_style(tree_style):
    # add title to header and footer
    text = TextFace("Frequence", min_fsize=5, max_fsize=12, width=50, rotation=0)
    tree_style.aligned_panel_header.add_face(text, column=0)
    
    tree_style.add_legend(
            title = "Frequence", 
            variable='continuous', 
            value_range=[0, 1],
            color_range=["darkred", "white"]
            )    
    return 

# define node Face layout function
def layout_heatmap(mincolor, maxcolor):
    #maxval = max(node.props.get('frequence') for node in t.leaves())
    maxval = 1
    minval = 0

    def color_gradient(c1, c2, mix=0):
        """ Fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1) """
        c1 = np.array(mpl.colors.to_rgb(c1))
        c2 = np.array(mpl.colors.to_rgb(c2))
        return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

    def get_heatmapface(node):
        if node.is_leaf:
            ratio = float(node.props.get('frequence')) / maxval
            gradient_color = color_gradient(mincolor, maxcolor, mix=ratio)
            print_frequnce = f"{node.props.get('frequence'):.2%}"
            rect_face = RectFace(
                width=50, height=70, color=gradient_color,
                opacity=0.7, text=print_frequnce, fgcolor='black',
                min_fsize=6, max_fsize=15, ftype='sans-serif',
                padding_x=0, padding_y=0,
                tooltip=None)
            node.add_face(rect_face, position='aligned', column=0)
        return 
    return get_heatmapface

# Create a TreeLayout object, passing in the function
barplot_layout = TreeLayout(
    name='HeatMap',
    ns=layout_heatmap(mincolor='white', maxcolor='darkred'), 
    ts=layout_tree_style,
    aligned_faces=True)

# add layout to layouts list
layouts = []
layouts.append(barplot_layout)
t.explore(
    layouts=layouts, 
    include_props=("name", "dist", "frequence"),
    keep_server=True)

