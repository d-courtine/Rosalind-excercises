#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO
from Bio.Seq import Seq

f = open('rosalind_filt.txt', 'r')
first_line = f.readline().rstrip()
threshold = first_line.split()
for i in range(0, len(threshold)):
   threshold[i] = int(threshold[i]) 

seqQual = 0
records = SeqIO.parse(f, 'fastq')
for record in records:
    count = 0
    for i in record.letter_annotations['phred_quality']:
        if i < threshold[0]:
            count += 1
    val = ((100-threshold[1])*len(record.letter_annotations['phred_quality']))/100
    if count <= val :
        seqQual += 1
print(seqQual)

