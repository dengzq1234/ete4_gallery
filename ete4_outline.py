#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, OutlineFace


TREEFILE = 'example_data/tree.nw'

<<<<<<< HEAD
popup_prop_keys = [
                'name', 'dist', 'support', 'sample1',
                'sample2','sample3','sample4','sample5',
                'random_type','bool_type','bool_type2'
        ]

t = Tree(open(TREEFILE))
level = 2 #level 1 is leaf name

def get_outlineface(): # work on internal node of collapse face
    def layout_fn(node):
        color="green"
        if not node.is_root:
            #face_name = TextFace(node.props.get('sci_name'), color=color)
            #face_name = OutlineFace(node.props.get('sci_name'), color=color, collapsing_height= float("inf"))
            face_name = OutlineFace(stroke_color='red', color=color,
                #collapsing_height= float("inf"),
                opacity=1.0, stroke_width=500, )
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = color
            node.add_face(face_name, column = 0,  position = 'branch_right', collapsed_only=True)
    return layout_fn
    return
=======
t = Tree(open(TREEFILE))

def layout_outline(node):
    color="green"
    if not node.is_root:
        face = OutlineFace(
            stroke_color='red',
            color='green',
            collapsing_height=float("inf"),
            opacity=1.0, stroke_width=500)

        node.sm_style["draw_descendants"] = False
        node.sm_style["outline_color"] = 'green'

        node.add_face(face, position='branch_right', collapsed_only=True)
>>>>>>> 3d1e59cab10e9cdd815ee5a6c879c957453a488f


layouts = [
    TreeLayout(name='sample1', ns=layout_outline, aligned_faces=True),
]

<<<<<<< HEAD
t.explore(daemon=False, layouts=layouts, compress=False)
=======
t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
>>>>>>> 3d1e59cab10e9cdd815ee5a6c879c957453a488f
