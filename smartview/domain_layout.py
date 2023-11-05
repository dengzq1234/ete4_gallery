from ete4 import Tree
from ete4.smartview import TreeLayout, SeqFace, SeqMotifFace, AlignmentFace

# Create a random tree and add to each leaf a random set of motifs
# from the original set
t = Tree("((A, B, C, D, E, F, G), H, I);")

seq = ("-----------------------------------------------AQAK---IKGSKKAIKVFSSA---"
      "APERLQEYGSIFTDA---GLQRRPRHRIQSK-------ALQEKLKDFPVCVSTKPEPEDDAEEGLGGLPSN"
      "ISSVSSLLLFNTTENLYKKYVFLDPLAG----THVMLGAETEEKLFDAPLSISKREQLEQQVPENYFYVPD"
      "LGQVPEIDVPSYLPDLPGIANDLMYIADLGPGIAPSAPGTIPELPTFHTEVAEPLKVGELGSGMGAGPGTP"
      "AHTPSSLDTPHFVFQTYKMGAPPLPPSTAAPVGQGARQDDSSSSASPSVQGAPREVVDPSGGWATLLESIR"
      "QAGGIGKAKLRSMKERKLEKQQQKEQEQVRATSQGGHL--MSDLFNKLVMRRKGISGKGPGAGDGPGGAFA"
      "RVSDSIPPLPPPQQPQAEDED----")

mixed_motifs = [
        # seq.start, seq.end, shape, width, height, fgcolor, bgcolor
        [10, 100, "[]", None, 20, "black", "rgradient:blue", "arial|8|white|long text clipped long text clipped"],
        [101, 150, "o", None, 20, "blue", "pink", None],
        [155, 180, "()", None, 20, "blue", "rgradient:purple", None],
        [160, 190, "^", None, 24, "black", "yellow", None],
        [191, 200, "<>", None, 22, "black", "rgradient:orange", None],
        [201, 250, "o", None, 22, "black", "brown", None],
        [351, 370, "v", None, 25, "black", "rgradient:gold", None],
        [370, 420, "compactseq", 5, 10, None, None, None],
]

simple_motifs = [
        # seq.start, seq.end, shape, width, height, fgcolor, bgcolor
        [10, 60, "[]", None, 20, "black", "rgradient:blue", "arial|8|white|long text clipped long text clipped"],
        [120, 150, "o", None, 20, "blue", "pink", None],
        [200, 300, "()", None, 20, "blue", "red", "arial|8|white|hello"],
]

box_motifs = [
        # seq.start, seq.end, shape, width, height, fgcolor, bgcolor
        [0,  5, "[]", None, 20, "black", "rgradient:blue", "arial|8|white|10"],
        [10, 25, "[]", None, 20, "black", "rgradient:ref", "arial|8|white|10"],
        [30, 45, "[]", None, 20, "black", "rgradient:orange", "arial|8|white|20"],
        [50, 65, "[]", None, 20, "black", "rgradient:pink", "arial|8|white|20"],
        [70, 85, "[]", None, 20, "black", "rgradient:green", "arial|8|white|20"],
        [90, 105, "[]", None, 20, "black", "rgradient:brown", "arial|8|white|20"],
        [110, 125, "[]", None, 20, "black", "rgradient:yellow", "arial|8|white|20"],
]

def layout_domain(node):
    if node.name == 'A':
        seq_face = SeqMotifFace(seq, width=1000, gapcolor="red")
        node.add_face(seq_face, position='aligned')
    elif node.name == 'B':
        seq_face = SeqMotifFace(seq, seq_format="line", width=1000, gap_format="blank")
        node.add_face(seq_face, position='aligned')
    elif node.name == 'C':
        seq_face = SeqMotifFace(seq, seq_format="line", width=1000)
        node.add_face(seq_face, position='aligned')
    elif node.name == 'D':
        seq_face = SeqMotifFace(seq, seq_format="()", width=1000)
        node.add_face(seq_face, position='aligned')
    elif node.name == 'E':
        seq_face = SeqMotifFace(seq, motifs=simple_motifs, seq_format="-", width=1000)
        node.add_face(seq_face, position='aligned')
    elif node.name == 'F':
        seq_face = SeqMotifFace(seq, motifs=simple_motifs, gap_format="blank", width=1000)
        node.add_face(seq_face, position='aligned')
    elif node.name == 'G':
        seq_face = SeqMotifFace(seq, motifs=mixed_motifs, seq_format="-", width=1000)
        node.add_face(seq_face, position='aligned')
    elif node.name == 'H':
        seq_face = SeqMotifFace(seq=None, motifs=box_motifs, gap_format="line", width=1000)
        node.add_face(seq_face, position='aligned')
    elif node.name == 'I':
        seq_face = SeqMotifFace(seq[30:60], seq_format="seq")
        node.add_face(seq_face, position='aligned')
    return

layouts = [
    TreeLayout(name='layout_domain', ns=layout_domain, aligned_faces=True),    
]
t.explore(layouts=layouts, keep_server=True)