import random

from ete4 import Tree
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import RectFace, HTMLFace


t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)


def get_face(node):
    if node.is_leaf:
        val = node.name
        html_content = "<p>This is {}</p>".format(str(val))
        face = HTMLFace(html=html_content,
        width=100, height=100, name=val,
        padding_x=2, padding_y=2)
        node.add_face(face, position="aligned")
    return


layouts = [
    TreeLayout(name='sample1', ns=get_face, aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
