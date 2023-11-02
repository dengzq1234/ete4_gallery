from ete4 import Tree
from ete4.smartview import TreeLayout

t = Tree('((a,b),c);')

# Draw nodes as small red square of diameter equal fo 10 pixels
def modify_node_style(node):
    # Draw nodes as small red square of diameter equal fo 10 pixels
    # Create an independent node style for each node, which is
    # initialized with a red foreground color.
    node.sm_style["fgcolor"] = "red"
    node.sm_style["shape"] = "circle"
    node.sm_style["size"] = 10

    # Let's now modify the aspect of the root node
    # we set the foreground color to blue and the size to 30 for the root node
    
    # Check if the node is the root node
    if node.is_root:
        node.sm_style["fgcolor"] = "blue"
        node.sm_style["size"] = 30
        node.sm_style["vt_line_type"] = 2
        node.sm_style["vt_line_width"] = 10
        node.sm_style["vt_line_color"] = "#964B00"
    return

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_node_style)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)
