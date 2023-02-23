from ete4 import Tree
# from staple_layouts import LayoutBarplot
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import CircleFace, PieChartFace



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
            piechart_data = [
                ["pie1", 4, "red", None],
                ["pie2", 10, "blue", None],
                ["pie3", 20, "green", None],
                ]
            face = PieChartFace(radius=20, data=piechart_data, name=prop, 
            padding_x=2,padding_y=2,tooltip=None)
            node.add_face(face, position="aligned", column=level)
    return layout_fn


layouts = [
    TreeLayout(name='sample1', ns=get_face(level, 'sample1'), aligned_faces = True),
]

t.explore(tree_name='example',layouts=layouts, \
            popup_prop_keys=popup_prop_keys, port=5000)