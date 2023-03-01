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


def get_attrface(level, prop):
    def layout_fn(node):
        if node.is_leaf():
            attr_face = AttrFace(node.props.get(prop), name="sample1",
            color="red",
            min_fsize=6, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0)
            node.add_face(attr_face, position="aligned", column=level)
    return layout_fn

layouts = [
    # Rectangular face
    TreeLayout(name='sample1', ns=get_attrface(level, 'sample1'),aligned_faces = True),
]

t.explore(tree_name='example',layouts=layouts, \
            popup_prop_keys=popup_prop_keys, port=5000)
