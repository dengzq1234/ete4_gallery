import argparse
from ete4 import Tree
from ete4.smartview import TreeStyle, TreeLayout

# Set up argument parser
parser = argparse.ArgumentParser(description='Modify tree style based on command line flag.')
parser.add_argument('--ultrametric', action='store_true', help='Set the tree to be ultrametric.')

# Parse arguments
args = parser.parse_args()

# Create your tree
t = Tree()
t.populate(100, random_branches=True)

# Function to modify the tree style
def modify_tree_style(tree_style):
    # tree_style.aligned_grid = False
    tree_style.collapse_size = 20
    tree_style.ultrametric = args.ultrametric  # Set based on command line flag

# Function to modify the tree style
def add_legend_style(tree_style):
    # add legend
    tree_style.collapse_size = 90
    tree_style.add_legend(
        title="MyLegend", 
        variable="discrete", 
        colormap={"a":"red", "b":"blue", "c":"green"}
        )


# Create a TreeLayout object, passing in the function
tree_layout = TreeLayout(name="MyTreeLayout", ts=modify_tree_style)
tree_layout2 = TreeLayout(name="MyTreeLayout2", ts=add_legend_style)

# Add the layout to a list
layouts = [tree_layout2, tree_layout]

# Explore the tree with the specified layout
t.explore(keep_server=True, layouts=layouts)