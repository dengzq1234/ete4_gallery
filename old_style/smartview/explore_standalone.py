from ete4 import Tree
t = Tree('((a,b),c);')
#t.render("tree")
t.explore(keep_server=False)
