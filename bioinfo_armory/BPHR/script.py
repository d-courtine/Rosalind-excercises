#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO
from Bio.Seq import Seq

f = open('rosalind_bphr.txt', 'r')
#f = open('test.txt', 'r')
threshold = f.readline().rstrip()
threshold = int(threshold)

seqCount = 0
mean = 0
table = []
first = True

records = SeqIO.parse(f, 'fastq')
for record in records:
    # Init table to the right lenght
    if first:
        for i in range(0, len(record.letter_annotations['phred_quality'])):
            table.append(0)
        first = False

    for i in range(0, len(record.letter_annotations['phred_quality'])):
        table[i] += record.letter_annotations['phred_quality'][i]

    seqCount +=1

for i in range(0, len(table)):
    if (table[i] / seqCount) < threshold:
        mean += 1

print(mean)

