#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeStyle, TreeLayout

t = Tree()
t.populate(20, random_branches=True)

def modify_tree_style(tree_style):
    #tree_style.aligned_grid = False
    tree_style.collapse_size = 70


# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ts=modify_tree_style)

layouts = [tree_layout]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
