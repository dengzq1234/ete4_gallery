from ete4 import Tree
from ete4.smartview import TreeLayout

t = Tree('((A,B),C);')

# Draw nodes as small red square of diameter equal fo 10 pixels
def modify_node_style(node):
    # Draw nodes as small red square of diameter equal fo 10 pixels
    node.sm_style["fgcolor"] = "red"
    node.sm_style["shape"] = "traingle"
    node.sm_style["size"] = 10

    # brown dashed branch lines with width equal to 2 pixels
    node.sm_style["hz_line_type"] = 1
    node.sm_style["hz_line_width"] = 2
    node.sm_style["hz_line_color"] = "#964B00"
    return

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=modify_node_style)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)
