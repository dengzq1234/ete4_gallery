from ete4 import Tree
from ete4.smartview import Layout

t = Tree('((a,b),c);')

# Nodes will be represented as small red triangles of 5 pixels radius.
style_dot = {'shape': 'triangle',
                      'radius': 5,
                      'fill': 'red'}

# Branch lines (horizontal lines) will be brown and dashed, and 10 pixels thick.
style_hz_line = {'stroke-dasharray': '5,5',
                 'stroke-width': 10,
                 'stroke': '#964B00'}

def draw_node(node):
    if node.is_leaf:
        return {'dot': style_dot,
                'hz-line': style_hz_line}

layout = Layout(name='My layout', draw_node=draw_node)
t.explore(layouts=[layout])
input()