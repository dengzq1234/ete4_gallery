from ete4 import Tree
from ete4 import SeqGroup

# from staple_layouts import LayoutBarplot
from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import SeqFace, SeqMotifFace, AlignmentFace
from collections import defaultdict

TREEFILE = './basic_example1_annotated.nw'
MSA = "./basic_example1_annotated.aln.faa"
PROTEIN2DOMAIN = "./NUP62.pfams"

popup_prop_keys = [
                'name', 'dist', 'support', 'sample1',
                'sample2','sample3','sample4','sample5',
                'random_type','bool_type','bool_type2',
                'seq'
        ]


t = Tree(TREEFILE, format=1)
level = 2 #level 1 is leaf name


def parse_fasta(fastafile):
    fasta_dict = {}
    with open(fastafile,'r') as f:
        head = ''
        seq = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq != '':
                    fasta_dict[head] = seq
                    seq = ''
                    head = line[1:]
                else:
                    head = line[1:]
            else:
                seq += line
    fasta_dict[head] = seq
    return fasta_dict

def parse_pfams(pfamoutput):
    """
    output:
        {
            leaf_node: [[domain1, start, end],[domain2, start,end]],
            leaf_node2: [[domain1, start, end],[domain2, start,end]],
        }
    example:
        {
            'Phy003I7ZJ_CHICK': [['Nsp1_C', '7', '116']], 
            'Phy0054BO3_MELGA': [['Nsp1_C', '3', '116']], 
            'Phy00508FR_NIPNI': [['Nsp1_C', '3', '116']], 
            'Phy004O1E0_APTFO': [['Nsp1_C', '2', '116']],
            ....
        }
    """
    protein2domain = {}
    #domains = defaultdict(list)
    with open(pfamoutput,'r') as f:
        for line in f:
            if line.startswith("#"):
                pass
            else:
                line = line.rstrip()
                name = line.split('\t')[0]
                hit = line.split('\t')[1]
                start = line.split('\t')[5]
                end = line.split('\t')[6]
                if name not in protein2domain:
                    protein2domain[name] = []
                    # domains = {}

                    # if hit in domains:
                    #     domains[hit].append((start, end))
                    # else:
                    #     domains[hit]= [(start, end)]
                    protein2domain[name].append([hit, start, end])
                else:
                    #domains[hit].append((start, end))
                    protein2domain[name].append([hit, start, end])

    return protein2domain

name2pfams = parse_pfams(PROTEIN2DOMAIN)
name2seq = parse_fasta(MSA)
for leaf in t.iter_leaves():
    leaf.add_prop('seq', name2seq[leaf.name])

def get_alnface():
    def layout_fn(node):
        if node.is_leaf():
            seq = node.props.get('seq')
            seq_face = AlignmentFace(seq, seqtype='aa',
            gap_format='line', seq_format='[]',
            width=None, height=None, # max height
            fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
            gap_linewidth=0.2,
            max_fsize=12, ftype='sans-serif',
            padding_x=0, padding_y=0)
            node.add_face(seq_face, position="aligned", column=level)
    return layout_fn

def get_seqface():
    def layout_fn(node):
        if node.is_leaf():
            seq = node.props.get('seq')
            seq_face = SeqFace(seq, seqtype='aa', poswidth=15,
            draw_text=True, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0)
            node.add_face(seq_face, position="aligned", column=level)
    return layout_fn

def get_seqmotifface():
    def layout(node):
        if node.is_leaf():
            if node.name in name2pfams:
                seq = name2seq[node.name]
                protDomains = name2pfams[node.name]
                doms = []
                for name, start, end in  protDomains:
                    color = "gray"
                    dom = [int(start), int(end), "()", 
                            None, None, color, color,
                            "arial|20|black|%s" %(name)]
                    #[3, 116, '()', None, None, 'gray', 'gray', 'arial|20|black|Nsp1_C']
                    doms.append(dom)

                seqFace = SeqMotifFace(seq, motifs=doms, seqtype='aa', 
                        gap_format='line', seq_format='[]', 
                        width=None, height=None, # max height
                        fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
                        gap_linewidth=0.2,
                        max_fsize=12, ftype='sans-serif',
                        padding_x=0, padding_y=0)

                node.add_face(seqFace, position="aligned", column=0)
    return layout

layouts = [
    
    TreeLayout(name='aln', ns=get_alnface(), aligned_faces = True),
    TreeLayout(name='seq', ns=get_seqface(), aligned_faces = True),
    TreeLayout(name='pfam', ns=get_seqmotifface(), aligned_faces = True),
]

t.explore(tree_name='example',layouts=layouts, \
            popup_prop_keys=popup_prop_keys, port=5000)