#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, RectFace, TextFace
import random

t = Tree('((((a1,a2),a3), ((b1,b2),(d1,d2))), ((c1,c2),c3));')

# find common ancestors and annotate them
n1 = t.common_ancestor(["a1", "a2", "a3"])
n2 = t.common_ancestor(["b1", "b2"])
n3 = t.common_ancestor(["c1", "c2", "c3"])
n4 = t.common_ancestor(["d1", "d2"])
n1.name = "ancestor_a"
n2.name = "ancestor_b"
n3.name = "ancestor_c"
n4.name = "ancestor_d"

# set color map dictionary
colormap = {
    "ancestor_a": "LightSteelBlue",
    "ancestor_b": "Moccasin",
    "ancestor_c": "DarkSeaGreen",
    "ancestor_d": "Brown"
}

def get_tree_style(colormap):
    def add_legend(tree_style):
        tree_style.add_legend(
            title = "MyLegend", 
            variable = "discrete", 
            colormap = colormap
            )
        return
    return add_legend

def get_node_face(colormap):
    def get_background(node):
        # make outline face
        if node.name in colormap:
            lca_face = RectFace(
                width=20, 
                height=None, # circular  
                color=colormap.get(node.name),
                opacity=0.7, 
                text=node.name, 
                fgcolor='white',
                min_fsize=6, 
                max_fsize=15, 
                ftype='sans-serif',
                padding_x=1, 
                padding_y=1,
                tooltip=None)
            lca_face.rotate_text = True

            # collapsed nodes
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = colormap.get(node.name)

            # show text face
            node.add_face(lca_face, position='aligned', column=0)
            # show text face even for collapsed nodes
            node.add_face(lca_face, position='aligned', collapsed_only=True)
            
            
        return get_background
    return get_background
    

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(
    name="MyTreeLayout", 
    ns=get_node_face(colormap), 
    ts=get_tree_style(colormap),
    active=True,
    aligned_faces=True)

layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)