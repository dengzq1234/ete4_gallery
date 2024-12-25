from ete4 import Tree
t = Tree()
t.populate(10, random_branches=True)

t.explore(show_leaf_name=True, show_branch_length=True, show_branch_support=True, keep_server=True)
