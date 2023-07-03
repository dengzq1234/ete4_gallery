#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, TextFace, RectFace
import numpy as np
import matplotlib as mpl

TREEFILE = 'example_data/tree.nw'

color_dict = {
    "high":"red",
    "medium":"blue",
    "low": "green",
}

t = Tree(open(TREEFILE))
level = 2  # level 1 is leaf name

class LayoutText(TreeLayout):
    def __init__(self, name, column, color_dict, text_prop, width=70, min_fsize=5, max_fsize=15, legend=True):
        super().__init__(name)
        self.aligned_faces = True
        self.text_prop = text_prop
        self.column = column
        self.color_dict = color_dict
        self.internal_prop = text_prop+'_counter'
        self.legend = legend
        self.width = width
        self.height = None
        self.min_fsize = min_fsize
        self.max_fsize = max_fsize
        self.absence_color = "#EBEBEB"
        self.padding_x = 1
        self.padding_y = 0

    def set_tree_style(self, tree, tree_style):
        super().set_tree_style(tree, tree_style)
        text = TextFace(self.text_prop, min_fsize=self.min_fsize, max_fsize=self.max_fsize, padding_x=2, width=self.width, rotation=315)
        tree_style.aligned_panel_header.add_face(text, column=self.column)

        if self.legend:
            if self.color_dict:
                tree_style.add_legend(title=self.text_prop,
                                    variable='discrete',
                                    colormap=self.color_dict
                                    )

    def set_node_style(self, node):
        if node.is_leaf and node.props.get(self.text_prop):
            prop_text = node.props.get(self.text_prop)
            if prop_text:
                if type(prop_text) == list:
                    prop_text = ",".join(prop_text)
                else:
                    pass
                if self.color_dict:
                    prop_face = TextFace(prop_text, color=self.color_dict.get(prop_text, 'black'),min_fsize=self.min_fsize, max_fsize=self.max_fsize, padding_x=2, width=self.width )
                else:
                    prop_face = TextFace(prop_text, color='black', min_fsize=self.min_fsiz, max_fsize=self.max_fsize, padding_x=2, width=self.width )
            node.add_face(prop_face, column=self.column, position="aligned")

class LayoutHeatmap(TreeLayout):
    def __init__(self, name=None, column=0, width=70, height=None, internal_rep='', \
        prop=None, maxval=100, minval=0, min_color="#ffffff", max_color="#971919",\
        legend=True):
        super().__init__(name)
        self.aligned_faces = True
        self.num_prop = prop
        self.column = column
        #self.colour_dict = colour_dict
        self.min_color = min_color
        self.max_color = max_color
        self.maxval = maxval
        self.minval = minval
        self.internal_prop = prop+'_'+internal_rep
        self.width = width
        self.height = height
        self.padding_x = 1
        self.padding_y = 1
        self.min_fsize = 5
        self.max_fsize = 15

    def set_tree_style(self, tree, tree_style):
        super().set_tree_style(tree, tree_style)
        text = TextFace(self.num_prop, min_fsize=self.min_fsize, max_fsize=self.max_fsize, padding_x=self.padding_x, width=self.width, rotation=315)
        tree_style.aligned_panel_header.add_face(text, column=self.column)

        if self.legend:
            colormap = { self.num_prop: {self.max_color},
                        }
            tree_style.add_legend(title=self.num_prop,
                                    variable='continuous',
                                    colormap=colormap,
                                    value_range=[self.minval, self.maxval],
                                    color_range=[self.min_color, self.max_color]
                                    )

    def set_node_style(self, node):
        c1 = self.min_color
        c2 = self.max_color #red
        if node.is_leaf and node.props.get(self.num_prop):
            # heatmap

            tooltip = ""
            if node.name:
                tooltip += f'<b>{node.name}</b><br>'
            if self.num_prop:
                tooltip += f'<br>{self.num_prop}: {node.props.get(self.num_prop)}<br>'

            try:
                ratio = float(node.props.get(self.num_prop)) / self.maxval
                gradient_color = color_gradient(c1, c2, mix=ratio)
                identF = RectFace(width=self.width, height=self.height, text="%.2f" % (float(node.props.get(self.num_prop))), color=gradient_color,
                    padding_x=self.padding_x, padding_y=self.padding_y, tooltip=tooltip)

            except ValueError: # for miss data
                identF = RectFace(width=self.width, height=self.height, text="NA", color=c1,
                padding_x=self.padding_x, padding_y=self.padding_y, tooltip=tooltip)

            node.add_face(identF, column = self.column,  position = 'aligned')

def color_gradient(c1, c2, mix=0):
    """ Fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1) """
    # https://stackoverflow.com/questions/25668828/how-to-create-colour-gradient-in-python
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

layouts = [
    LayoutText(name='random_type', column=level, color_dict=color_dict, text_prop="random_type", width=70, min_fsize=5, max_fsize=15, legend=True),
    LayoutHeatmap(name='Heatmap_sample1', column=level+1, width=70, internal_rep='', prop='sample1', maxval=1, minval=0)
]

t.explore('example', layouts=layouts)
