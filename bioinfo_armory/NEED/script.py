#!/usr/bin/env python3

from Bio import Entrez
from Bio import SeqIO
from Bio.Emboss.Applications import NeedleCommandline
from Bio import AlignIO
import time
import os

####### Imput #######
infile = 'rosalind_need.txt'
seqsId = open(infile, 'r').read().split()

out1 = 'sequence1.fa'
out2 = 'sequence2.fa'
outfile1 = open(out1, 'w')
outfile2 = open(out2, 'w')

####### Main #######
Entrez.email = "damien.courtine@univ-brest.fr"

first = True

for i in seqsId:
    handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
    records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
    for record in records:
        if first:
            print(">{}\n{}".format(record.description, record.seq), file=outfile1)
            first = False
        else:
            print(">{}\n{}".format(record.description, record.seq), file=outfile2)

    time.sleep(1)

outfile1.close()
outfile2.close()


needle_cline = NeedleCommandline(asequence=out1, bsequence=out2,\
        gapopen=10, gapextend=1, outfile="needle.txt", endweight='y', endopen=10, endextend=1)
print(needle_cline)

std_output, err_output = needle_cline.__call__()
print(std_output + err_output)

####### Read the alignment file #######
align = AlignIO.read("needle.txt", "emboss")

# the score and other qualifiers is not present in 'records', but in 'annotations'
print(int(align.annotations['score']))

####### Clear #######
os.remove(out1)
os.remove(out2)
os.remove('needle.txt')


