#!/usr/bin/env python
# -*- coding:utf-8 -*

from Bio import Entrez
from Bio import SeqIO

### Best way to read a 3-lines file:
## genus, start, end = open('GBK.txt').read().split('\n')

f=open('rosalind_frmt.txt', 'r')

temp = (f.read().rstrip('\n'))
requestId = temp.split()

Entrez.email = "damien.courtine@univ-brest.fr"

seq_dict = {}
for i in requestId:
    handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
    records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
    for record in records:
        seq_dict[record.description] = record.seq

smallest_seq_id = ""
length_keep = 10000000000000000

for item, value in seq_dict.items():
    if len(value) <= length_keep:
        smallest_seq_id = item
        length_keep = len(value)

print(">%s" % smallest_seq_id, "\n%s" %seq_dict[smallest_seq_id])


