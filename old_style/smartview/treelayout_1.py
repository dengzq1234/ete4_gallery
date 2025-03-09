from ete4 import Tree
from ete4.smartview import TreeLayout

t = Tree()
t.populate(20, random_branches=True)

# define a TreeLayout
tree_layout = TreeLayout(name="MyTreeLayout")

# add TreeLayout to layouts
layouts = []
layouts.append(tree_layout)

# explore tree
t.explore(keep_server=True, layouts=layouts)