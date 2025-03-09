from ete4 import Tree
from ete4.smartview import TreeLayout, NodeStyle

t = Tree('((A,B),C);')

# Draw nodes as small red square of diameter equal fo 10 pixels
triangle_node_style = NodeStyle()
triangle_node_style["shape"] = "triangle"
triangle_node_style["size"] = 10
triangle_node_style["fgcolor"] = "red"

# brown dashed branch lines with width equal to 2 pixels
triangle_node_style["hz_line_type"] = 1
triangle_node_style["hz_line_width"] = 2
triangle_node_style["hz_line_color"] = "#964B00"

# Applies the same static style to all nodes in the tree. Note that,
def modify_node_style(node):
    node.set_style(triangle_node_style)
    return

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_node_style)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)
