from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace

t = Tree('((((a,b),c),d),e);')


class MyTreeLayout(TreeLayout):
    def __init__(self, name="My First TreeLayout", min_fsize=5, max_fsize=12, 
            width=50, rotation=0, vowel_color="red", conostant_color="blue", 
            vowel_node_size=5, conostant_node_size=5, aligned_faces=True,
            column=0):
        
        # Ensuring that any initialization that TreeLayout needs to do is done, 
        # before MyTreeLayout goes on to do its own additional initialization. 
        super().__init__(name, aligned_faces=True) 

        self.name = name
        self.min_fsize = min_fsize
        self.max_fsize = max_fsize
        self.width = width
        self.rotation = rotation

        self.vowel_color = vowel_color
        self.conostant_color = conostant_color
        self.vowel_node_size = vowel_node_size
        self.conostant_node_size = conostant_node_size
        self.aligned_faces = aligned_faces
        self.column = column


    def set_tree_style(self, tree, style):
        text = TextFace(self.name, min_fsize=self.min_fsize, 
            max_fsize=self.max_fsize, width=self.width, rotation=self.rotation)

        style.aligned_panel_header.add_face(text, column=self.column)
        style.add_legend(
            title=self.name,  
            variable="discrete", 
            colormap={"vowel":"red", "conostant":"blue"}
            )

    def set_node_style(self, node):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_textface = TextFace(
            text="vowel", color=self.vowel_color, 
            min_fsize=self.min_fsize, max_fsize=self.max_fsize,
            width=self.width, rotation=self.rotation
        )

        conostant_textface = TextFace(
            text="not vowel!", color=self.conostant_color, 
            min_fsize=self.min_fsize, max_fsize=self.max_fsize,
            width=self.width, rotation=self.rotation
        )

        # here to set the node style
        if node.is_leaf:
            if node.name in vowels:
                node.sm_style['size'] = self.vowel_node_size
                node.sm_style['fgcolor'] = self.vowel_color

                # here to add text face to node in aligned position
                node.add_face(vowel_textface, column=self.column, position='aligned')
            else:
                node.sm_style['size'] = self.conostant_node_size
                node.sm_style['fgcolor'] = self.conostant_color
                
                # here to add text face to node in aligned position
                node.add_face(conostant_textface, column=self.column, position='aligned')


# Create a TreeLayout object, passing in the function
tree_layout = MyTreeLayout(name="MyTreeLayout", aligned_faces=True)
layouts = []
layouts.append(tree_layout)
t.explore(keep_server=True, layouts=layouts)