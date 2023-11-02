from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace

t = Tree('((((a,b),c),d),e);')


def vowel_node_layout(node):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # here to set the node style
    if node.is_leaf:
        if node.name in vowels:
            node.sm_style['size'] = 15
            node.sm_style['fgcolor'] = 'red'


# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ns=vowel_node_layout)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)