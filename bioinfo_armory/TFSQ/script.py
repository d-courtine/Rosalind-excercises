#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO

records = SeqIO.parse('rosalind_tfsq.txt', 'fastq')
for record in records:
    print(">%s\n%s" %(record.id, record.seq))
#    print(record.letter_annotations["phred_quality"])
