from ete4 import Tree
from ete4.smartview import Layout, TextFace

t = Tree('((a:1,b:1)n1:1,c):1;', parser='name')

def draw_node(node, collapsed):
    if node.name == 'n1':
        if collapsed:
            return TextFace('n1 is collapsed', column=0, position='right')
        else:
            return TextFace('n1 is NOT collapsed', column=0, position='right')

layout = Layout(name='My layout', draw_node=draw_node)
t.explore(layouts=[layout])
input()