#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Bio import SeqIO
from Bio import Seq

"""
Delete the intron(s) and concatenate the exons
"""

# seqs = SeqIO.parse("data.txt", "fasta")
seqs = SeqIO.parse("rosalind_splc.txt", "fasta")

main_seq = None
introns = list()

for seq in seqs:
    if not main_seq:
        main_seq = str(seq.seq)
    else:
        introns.append(str(seq.seq))

previous_end = 0
final_seq = ''

for i in range(0, len(main_seq)):
    for j in introns:
        if main_seq[i: i + len(j)] == j:

            # First intron was found
            if not final_seq:
                final_seq = main_seq[:i]

            # Internal intron(s)
            else:
                final_seq += main_seq[previous_end: i]

            previous_end = i + len(j)

# Do not forget the last part
if previous_end < len(main_seq):
    final_seq += main_seq[previous_end:]

prot_seq = str(Seq.Seq(final_seq).translate())
if prot_seq.endswith("*"):
    print(prot_seq[:-1])
