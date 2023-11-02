#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, RectFace, TreeStyle, TextFace


TREEFILE = 'example_data/tree.nw'

<<<<<<< HEAD
popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2', 'sample3', 'sample4', 'sample5',
    'random_type', 'bool_type', 'bool_type2'
]


t = Tree(open(TREEFILE))
level = 2  # level 1 is leaf name
=======
>>>>>>> 3d1e59cab10e9cdd815ee5a6c879c957453a488f

t = Tree(open(TREEFILE))

def layout_rect(node):
    if not node.is_leaf:
<<<<<<< HEAD
        node.sm_style['fgcolor']="blue"
        node.sm_style['size']=3
        return
    
    color_dict = {
            "high":"red",
            "medium":"blue",
            "low":"green"
            }
    if node.props.get("random_type"):
        color = color_dict.get(node.props.get("random_type"),"gray") 
        rect_face = RectFace(
            width=50, height=70, color=color,
            opacity=0.7, text=None, fgcolor='black',
            min_fsize=6, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0,
            tooltip=None)
        
        node.add_face(rect_face, position='aligned', column=level)
    
def tree_style_hello(tree_style):
    
    text = TextFace("random_type", min_fsize=5, max_fsize=12, width=50, rotation=315)
    #tree_style=TreeStyle()
    tree_style.aligned_panel_header.add_face(text, 1)

    tree_style.add_legend(title="random_type",
                                   variable='discrete',
                                   colormap={
           "high":"red",
           "medium":"blue",
           "low":"green"
           })

    
=======
        return

    rect_face = RectFace(
        width=77, height=70, color='blue',
        opacity=0.7, text=None, fgcolor='black',
        min_fsize=6, max_fsize=15, ftype='sans-serif',
        padding_x=0, padding_y=0,
        tooltip=None)

    node.add_face(rect_face, position='aligned', column=0)

>>>>>>> 3d1e59cab10e9cdd815ee5a6c879c957453a488f

layouts = [
    TreeLayout(name='sample1',ns=layout_rect, ts=tree_style_hello, aligned_faces=True),
]

<<<<<<< HEAD
t.explore(keep_server=True, layouts=layouts)
=======
t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
>>>>>>> 3d1e59cab10e9cdd815ee5a6c879c957453a488f
