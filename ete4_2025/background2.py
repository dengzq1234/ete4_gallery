from ete4 import Tree
from ete4.smartview import Layout, TextFace

t = Tree('((((a1,a2),a3), ((b1,b2),(b3,b4))), ((c1,c2),c3));')

# Background colors.
style1 = {'box': {'fill': 'LightSteelBlue'}}
style2 = {'box': {'fill': 'Moccasin'}}
style3 = {'box': {'fill': 'DarkSeaGreen'}}
style4 = {'box': {'fill': 'Khaki'}}

# Find common ancestors.
n1 = t.common_ancestor(['a1', 'a2', 'a3'])
n2 = t.common_ancestor(['b1', 'b2', 'b3', 'b4'])
n3 = t.common_ancestor(['c1', 'c2', 'c3'])
n4 = t.common_ancestor(['b3', 'b4'])

def draw_node(node):
    # Add node name with big text.
    yield TextFace(node.name, fs_min=6, fs_max=25, position='right')

    # Set the node style.
    if node == n1:
        yield style1
    elif node == n2:
        yield style2
    elif node == n3:
        yield style3
    elif node == n4:
        yield style4

layout = Layout('My layout', draw_node=draw_node)
t.explore(layouts=[layout])
input()