from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace

t = Tree('((a:1,b:1)n1:1,c):1;')

# Draw nodes text face in node with name n1
def modify_face_position(node):
    # find node with name n1
    if node.name == "n1":
        # write text face "Hola" in node n1 and show it in branch_right directly
        node.add_face(TextFace("Hola!", color="red"), column=0, position='branch_right', collapsed_only=False)
        # write text face "Hola" in node n1 and show it in branch_right only when node is collapsed
        node.add_face(TextFace('mundo!', color="blue"), column=1, position='branch_right', collapsed_only=True)
    return

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_face_position)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)