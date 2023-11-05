from ete4 import Tree
from ete4.smartview import TreeLayout, NodeStyle, TextFace

t = Tree('((((a1,a2),a3), ((b1,b2),(b3,b4))), ((c1,c2),c3));')

# set background color for difference node style
nst1 = NodeStyle()
nst1["bgcolor"] = "LightSteelBlue"
nst2 = NodeStyle()
nst2["bgcolor"] = "Moccasin"
nst3 = NodeStyle()
nst3["bgcolor"] = "DarkSeaGreen"
nst4 = NodeStyle()
nst4["bgcolor"] = "Khaki"

# find common ancestors
n1 = t.common_ancestor(["a1", "a2", "a3"])
n2 = t.common_ancestor(["b1", "b2", "b3", "b4"])
n3 = t.common_ancestor(["c1", "c2", "c3"])
n4 = t.common_ancestor(["b3", "b4"])

# set color map dictionary
colormap = {
    "ancestor_a": "LightSteelBlue",
    "ancestor_b": "Moccasin",
    "ancestor_c": "DarkSeaGreen",
    "ancestor_d": "Khaki"
}

def get_tree_style(colormap):
    def add_legend(tree_style):
        tree_style.add_legend(
            title = "MyLegend", 
            variable = "discrete", 
            colormap = colormap
            )
    return add_legend

def get_background(node):
    # make node name with bigger text
    node.add_face(TextFace(node.name, min_fsize=6, max_fsize=25), column=0, position="branch_right")
    # set node style
    if node == n1:
        node.set_style(nst1)
    elif node == n2:
        node.set_style(nst2)
    elif node == n3:
        node.set_style(nst3)
    elif node == n4:
        node.set_style(nst4)
    return 

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(
    name="MyTreeLayout", 
    ns=get_background, 
    ts=get_tree_style(colormap),
    active=True)

layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)