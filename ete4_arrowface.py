from ete4 import Tree
# from staple_layouts import LayoutBarplot
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import (RectFace, CircleFace, SeqMotifFace, AttrFace,
                        ArrowFace, TextFace, OutlineFace, LegendFace)



TREEFILE = './basic_example1_annotated.nw'

popup_prop_keys = [
                'name', 'dist', 'support', 'sample1',
                'sample2','sample3','sample4','sample5',
                'random_type','bool_type','bool_type2'
        ]

t = Tree(TREEFILE, format=1)
level = 2 #level 1 is leaf name

def get_face(level):
    def layout_fn(node):
        if node.is_leaf():
            face = ArrowFace(width=100, height=70, orientation='right',
            color='green', 
            stroke_color='gray', stroke_width='1.5px',
            text=None, fgcolor='black', # text color
            min_fsize=6, max_fsize=15,
            ftype='sans-serif',
            name="",
            padding_x=0, padding_y=0,
            tooltip=None)
            node.add_face(face, position="aligned", column=level)
    return layout_fn


layouts = [
    # Rectangular face
    TreeLayout(name='sample1', ns=get_face(level),aligned_faces = True),
]

t.explore(tree_name='example',layouts=layouts, \
            popup_prop_keys=popup_prop_keys, port=5000)