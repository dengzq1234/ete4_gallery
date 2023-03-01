from ete4 import Tree
# from staple_layouts import LayoutBarplot
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import (RectFace, CircleFace, SeqMotifFace, AttrFace,
                        TextFace, OutlineFace, LegendFace)



TREEFILE = 'example_data/tree.nw'

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
            text_face = TextFace(node.props.get(prop), color="black",
            min_fsize=6, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0, width=None, height=None)
            node.add_face(text_face, position="aligned", column=level)
    return layout_fn

layouts = [
    TreeLayout(name='sample1', ns=get_face(level, 'sample1'),aligned_faces = True),
]

t.explore(tree_name='example',layouts=layouts, \
            popup_prop_keys=popup_prop_keys, port=5000)
