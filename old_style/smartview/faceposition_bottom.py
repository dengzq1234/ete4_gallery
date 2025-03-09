from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace

t = Tree('((a:1,b:1):1,c:1)Root:1;')

# Draw nodes text face in root node
def modify_face_position(node):
    if node.is_root:
        node.add_face(TextFace("Hola!", color="red"), column=0, position='branch_bottom')
        # show mundo next to the hola
        node.add_face(TextFace('mundo!', color="blue"), column=1, position='branch_bottom')
        # show mundo under the hola
        #node.add_face(TextFace('mundo!', color="blue"), column=0, position='branch_bottom')
    return

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_face_position)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)
