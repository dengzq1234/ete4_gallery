from ete4 import Tree
# from staple_layouts import LayoutBarplot
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import OutlineFace



TREEFILE = 'example_data/tree.nw'

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


layouts = [
    # Rectangular face
    TreeLayout(name='sample1', ns=get_outlineface(), aligned_faces = True),
]

t.explore(daemon=False, layouts=layouts, compress=False)
