from ete4 import Tree
# from staple_layouts import LayoutBarplot
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import AlignLinkFace



TREEFILE = './basic_example1_annotated.nw'

popup_prop_keys = [
                'name', 'dist', 'support', 'sample1',
                'sample2','sample3','sample4','sample5',
                'random_type','bool_type','bool_type2'
        ]

t = Tree(TREEFILE, format=1)
level = 2 #level 1 is leaf name

def get_layout_align_link(stroke_color='blue', stroke_width=0.5,
            line_type=1, opacity=0.8):
    align_link_face = AlignLinkFace(stroke_color=stroke_color,
                                    stroke_width=stroke_width,
                                    line_type=line_type,
                                    opacity=opacity)
    def layout_fn(node):
        if node.is_leaf():
            node.add_face(align_link_face,
                          position='branch_right',
                          column=1e9)
        else:
            node.add_face(align_link_face,
                          position='branch_right',
                          column=1e9,
                          collapsed_only=True)
    layout_fn.__name__ = 'Aligned panel link'
    layout_fn._module = 'default'
    return layout_fn



layouts = [
    # Rectangular face
    TreeLayout(name='sample1', ns=get_layout_align_link(),aligned_faces = True),
]

t.explore(tree_name='example',layouts=layouts, \
            popup_prop_keys=popup_prop_keys, port=5000)