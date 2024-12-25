#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import TreeLayout, SeqFace, SeqMotifFace, AlignmentFace


TREEFILE = 'data/tree.nw'
MSA = 'data/tree.aln.faa'


t = Tree(open(TREEFILE))


def get_seqs(fastafile):
    """Read a fasta file and return a dict with d[description] = sequence.

    Example output: {'Phy003I7ZJ_CHICK': 'TMSQFNFSSAPAGGGFSFSTPKT...', ...}
    """
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



# get information alignment 
name2seq = get_seqs(MSA)


for leaf in t:
    leaf.add_prop('seq', name2seq[leaf.name])


def layout_alnface_gray(node):
    if node.is_leaf:
        seq_face = AlignmentFace(
            node.props.get('seq'),
            seqtype='aa', gap_format='line', seq_format='[]',
            width=800, height=None,
            fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
            gap_linewidth=0.2,
            max_fsize=12, ftype='sans-serif',
            padding_x=0, padding_y=0)

        node.add_face(seq_face, position='aligned')
    return

def layout_alnface_compact(node):
    if node.is_leaf:
        seq_face = AlignmentFace(
            node.props.get('seq'),
            seqtype='aa', gap_format='line', seq_format='compactseq',
            width=800, height=None,
            fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
            gap_linewidth=0.2,
            max_fsize=12, ftype='sans-serif',
            padding_x=0, padding_y=0)

        node.add_face(seq_face, position='aligned')
    return

def layout_seqface(node):
    if node.is_leaf:
       
        seq_face = SeqFace(
            node.props.get('seq'),
            seqtype='aa', poswidth=1, 
            draw_text=True, max_fsize=15, ftype='sans-serif',
            padding_x=0, padding_y=0)

        node.add_face(seq_face, position='aligned')
    return


layouts = [
    TreeLayout(name='compact_aln', ns=layout_alnface_compact, aligned_faces=True),
    TreeLayout(name='gray_aln', ns=layout_alnface_gray, aligned_faces=True, active=False),
    TreeLayout(name='seq', ns=layout_seqface, aligned_faces=True,  active=False),
]

t.explore(layouts=layouts, keep_server=True)
