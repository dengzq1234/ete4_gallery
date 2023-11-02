from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace

t = Tree('((a,b),c);')

# Draw nodes text face in leaf node
def modify_face_position(node):
    if node.is_leaf:
        node.add_face(TextFace("Hola!", color="red"), column=0, position='aligned')
        node.add_face(TextFace('mundo!', color="blue"), column=1, position='aligned')
    return

# set aligned_faces=True because we want to align the faces
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_face_position, aligned_faces=True)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)