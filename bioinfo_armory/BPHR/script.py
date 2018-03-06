#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO
from Bio.Seq import Seq

#f = open('rosalind_bphr.txt', 'r')
f = open('test.txt', 'r')
threshold = f.readline().rstrip()
threshold = int(threshold)

seqCount = 0
noPassBase = 0
records = SeqIO.parse(f, 'fastq')
for record in records:
    print(record.seq)
    print(record.letter_annotations['phred_quality'])
    seqCount += 1
    for pos in record.letter_annotations['phred_quality']:
        if pos < threshold:
            noPassBase += 1
print(noPassBase/seqCount)

