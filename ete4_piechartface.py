#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, PieChartFace, RectFace, Box
from ete4.smartview.renderer.draw_helpers import draw_rect
class StackedBarFace(RectFace):
    def __init__(self, width, height, data=None, name="", opacity=0.7, 
                min_fsize=6, max_fsize=15, ftype='sans-serif',
                padding_x=1, padding_y=0, tooltip=None):
        
        RectFace.__init__(self, width=width, height=height, name=name, color=None, 
            min_fsize=min_fsize, max_fsize=max_fsize, 
            padding_x=padding_x, padding_y=padding_y, tooltip=tooltip)
        
        self.width = width
        self.height = height

        # data = [ [name, value, color, tooltip], ... ]
        # self.data = [
        #     ['first', 10, 'red', None],
        #     ['second', 40, 'blue', None],
        #     ['green', 50, 'green', None]
        #     ]
        self.data = data
        

    def __name__(self):
        return "StackedBarFace"

    def draw(self, drawer):

        # Draw RectFace if only one datum

        if len(self.data) == 1:
            self.color = self.data[0][2]
            yield from RectFace.draw(self, drawer)

        else:
            total_value = sum(d[1] for d in self.data)
            start_x, start_y, dx, dy = self._box        
            
            for i in range(len(self.data)):
                i_value = self.data[i][1]
                color = self.data[i][2]
                
                if i > 0:
                    start_x += new_dx # start with where last segment ends
                
                new_dx = i_value/total_value * dx # width of segment
                
                self._box = Box(start_x,start_y,new_dx,dy)
                style = { 'fill': color }
                yield draw_rect(self._box,
                self.name,
                style=style,
                tooltip=self.tooltip)


TREEFILE = 'example_data/tree.nw'

t = Tree(open(TREEFILE))

def get_piechartface(prop):
    def layout_fn(node):
        if node.is_leaf:
            piechart_data = [
                ['pie1', 4, 'red', None],
                ['pie2', 10, 'blue', None],
                ['pie3', 20, 'green', None],
            ]
            face = PieChartFace(radius=30, data=piechart_data, name=prop,
                                padding_x=2, padding_y=2, tooltip=None)
            node.add_face(face, position='aligned')

    return layout_fn

def get_stackedbarface(prop):
    def layout_fn(node):
        if node.is_leaf:
            stackedbar_data = [
                ['pie1', 4, 'red', None],
                ['pie2', 10, 'blue', None],
                ['pie3', 20, 'green', None],
            ]
            # face = StackedBarFace(radius=30, data=piechart_data, name=prop,
            #                     padding_x=2, padding_y=2, tooltip=None)
            stackedbar_face = StackedBarFace(width=80, height=None, data=stackedbar_data, padding_x=2, padding_y=2)
            node.add_face(stackedbar_face, position='aligned')

    return layout_fn
layouts = [
    TreeLayout(name='sample1', ns=get_piechartface('sample1'), aligned_faces=True),
    TreeLayout(name='sample2', ns=get_stackedbarface('sample2'), aligned_faces=True),
]

t.explore(layouts=layouts)
input('Tree explorer running. Press enter to stop the server and finish.\n')
