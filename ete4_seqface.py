#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, SeqFace, SeqMotifFace, AlignmentFace


TREEFILE = 'basic_example1_annotated.nw'
MSA = 'basic_example1_annotated.aln.faa'
PROTEIN2DOMAIN = 'NUP62.pfams'

popup_prop_keys = [
    'name', 'dist', 'support', 'sample1',
    'sample2','sample3','sample4','sample5',
    'random_type','bool_type','bool_type2',
    'seq',
]


t = Tree(TREEFILE, format=1)
level = 2  # level 1 is leaf name


def get_seqs(fastafile):
    """Read a fasta file and return a dict with d[description] = sequence."""
    name2seq = {}
    seq = ''
    for line in open(fastafile):
        if line.startswith('>'):
            if seq:
                name2seq[head] = seq
                seq = ''
                head = line.lstrip('>').rstrip()
            else:
                head = line.lstrip('>').rstrip()
        else:
            seq += line.rstrip()
    name2seq[head] = seq
    return name2seq


def get_pfams(pfamoutput):
    """Read file pfamoutput and return a dict from protein to domain.

    Example output:
        #   leaf_node:          [(domain1, start1, end1), ...],
        {
            'Phy003I7ZJ_CHICK': [('Nsp1_C', 7, 116)],
            'Phy0054BO3_MELGA': [('Nsp1_C', 3, 116)],
            ...
        }
    """
    pfams = {}  # dict that maps protein names to domains
    for line in open(pfamoutput):
        if line.startswith('#'):
            continue
        name, hit, _, _, _, start, end, _ = line.rstrip().split('\t', 7)
        pfams.setdefault(name, []).append((hit, int(start), int(end)))

    return pfams


name2pfams = get_pfams(PROTEIN2DOMAIN)
name2seq = get_seqs(MSA)
for leaf in t.iter_leaves():
    leaf.add_prop('seq', name2seq[leaf.name])


def layout_alnface(node):
    if not node.is_leaf():
        return

    seq_face = AlignmentFace(
        node.props.get('seq'),
        seqtype='aa', gap_format='line', seq_format='[]',
        width=None, height=None,
        fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
        gap_linewidth=0.2,
        max_fsize=12, ftype='sans-serif',
        padding_x=0, padding_y=0)

    node.add_face(seq_face, position='aligned', column=level)


def layout_seqface(node):
    if not node.is_leaf():
        return

    seq_face = SeqFace(
        node.props.get('seq'),
        seqtype='aa', poswidth=15,
        draw_text=True, max_fsize=15, ftype='sans-serif',
        padding_x=0, padding_y=0)

    node.add_face(seq_face, position='aligned', column=level)


def layout_seqmotifface(node):
    if not node.is_leaf() or node.name not in name2pfams:
        return

    prot_domains = name2pfams[node.name]
    doms = [[start, end, '()',
             None, None, 'gray', 'gray',
             f'arial|20|black|{name}'] for name, start, end in prot_domains]

    seqFace = SeqMotifFace(
        name2seq[node.name],
        motifs=doms, seqtype='aa',
        gap_format='line', seq_format='[]',
        width=None, height=None,
        fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
        gap_linewidth=0.2,
        max_fsize=12, ftype='sans-serif',
        padding_x=0, padding_y=0)

    node.add_face(seqFace, position='aligned', column=0)


layouts = [
    TreeLayout(name='aln', ns=layout_alnface, aligned_faces=True),
    TreeLayout(name='seq', ns=layout_seqface, aligned_faces=True),
    TreeLayout(name='pfam', ns=layout_seqmotifface, aligned_faces=True),
]


t.explore(tree_name='example', layouts=layouts, popup_prop_keys=popup_prop_keys)
