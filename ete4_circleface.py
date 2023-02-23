from ete4 import Tree
# from staple_layouts import LayoutBarplot
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import (RectFace, CircleFace, SeqMotifFace, AttrFace,
                        TextFace, OutlineFace, LegendFace)



TREEFILE = './basic_example1_annotated.nw'

popup_prop_keys = [
                'name', 'dist', 'support', 'sample1',
                'sample2','sample3','sample4','sample5',
                'random_type','bool_type','bool_type2'
        ]

t = Tree(TREEFILE, format=1)
level = 2 #level 1 is leaf name

def get_face(level, prop):
    def layout_fn(node):
        if node.is_leaf():
            node_prop = float(node.props.get(prop)) * 15
            face = CircleFace(radius=node_prop, color="red", name=prop, 
            padding_x=2,padding_y=2,tooltip=None)
            node.add_face(face, position="aligned", column=level)
    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face(level, 'sample1'), aligned_faces = True),
]

t.explore(tree_name='example',layouts=layouts, \
            popup_prop_keys=popup_prop_keys, port=5000)