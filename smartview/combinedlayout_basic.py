from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace

t = Tree('((((a,b),c),d),e);')

def vowel_tree_style(tree_style):
    text = TextFace("Vowel title", min_fsize=5, max_fsize=12, width=50, rotation=0)
    tree_style.aligned_panel_header.add_face(text, column=0)
    tree_style.add_legend(
        title="MyLegend", 
        variable="discrete", 
        colormap={"vowel":"red", "conostant":"blue"}
        )

def vowel_node_layout(node):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # here to set the node style
    if node.is_leaf:
        if node.name in vowels:
            node.sm_style['size'] = 5
            node.sm_style['fgcolor'] = 'red'
            # here to add text face to node in aligned position
            node.add_face(TextFace('vowel!', color="red"), column=0, position='aligned')

        else:
            node.sm_style['size'] = 5
            node.sm_style['fgcolor'] = 'blue'   
            
            # here to add text face to node in aligned position
            node.add_face(TextFace('not vowel!', color="blue"), column=0, position='aligned')


# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", 
    ts=vowel_tree_style, 
    ns=vowel_node_layout,
    active=True, 
    aligned_faces=True)


layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)