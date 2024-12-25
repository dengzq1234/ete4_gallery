from ete4 import Tree
from ete4.smartview import TreeLayout, NodeStyle

t = Tree('((a,b),c);')

# Draw nodes as small red square of diameter equal fo 10 pixels
# Create an independent node style for each node, which is
# initialized with a red foreground color.
leaf_style = NodeStyle()
leaf_style["shape"] = "square"
leaf_style["size"] = 10
leaf_style["fgcolor"] = "red"

# we set the foreground color to blue and the size to 30 for the root node
root_style = NodeStyle()
root_style["fgcolor"] = "blue"
root_style["size"] = 30
root_style["vt_line_type"] = 2
root_style["vt_line_width"] = 10
root_style["vt_line_color"] = "#964B00"

# Draw nodes as small red square of diameter equal fo 10 pixels
def modify_node_style(node):
    # Let's now modify the aspect of the leaf nodes
    if node.is_leaf:
        node.set_style(leaf_style)
    # Let's now modify the aspect of the root node
    # Check if the node is the root node
    elif node.is_root:
        node.set_style(root_style)
    else:
        pass
    return

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_node_style)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)
