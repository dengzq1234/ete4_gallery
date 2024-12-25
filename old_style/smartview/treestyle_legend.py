from ete4 import Tree
from ete4.smartview import TreeStyle, TreeLayout, TextFace

t = Tree('((a,b),c);')
def modify_tree_style(tree_style):
    # add legend
    tree_style.add_legend(
        title="MyLegend", 
        variable="discrete", 
        colormap={"a":"red", "b":"blue", "c":"green"}
        )

# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ts=modify_tree_style)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)

