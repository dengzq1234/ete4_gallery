from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace

t = Tree('((a:1,b:1):1,c:1):1;')

# top_textface = TextFace(text="top!", color='blue',
#             min_fsize=6, max_fsize=25, ftype='courier',
#             padding_x=1, padding_y=1, width=None, rotation=90)

top_textface = TextFace(text="branch top!")
top_textface.color = 'blue'
top_textface.min_fsize = 6
top_textface.max_fsize = 25
top_textface.ftype = 'courier'
top_textface.padding_x = 0
top_textface.padding_y = 0
top_textface.width = None
top_textface.rotation = 0

# or all together
bottom_textface = TextFace(text="branch bottom!", color='red',
            min_fsize=6, max_fsize=25, ftype='sans-serif',
            padding_x=1, padding_y=1, width=None, rotation=0)


# Draw nodes text face in root node
def modify_face_property(node):
    node.add_face(top_textface, column=0, position='branch_top')
    node.add_face(bottom_textface, column=0, position='branch_bottom')
    return

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_face_property)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)
