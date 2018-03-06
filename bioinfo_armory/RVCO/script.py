#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO
from Bio.Seq import Seq

hitNbr = 0
records = SeqIO.parse('rosalind_rvco.txt', 'fasta')
for record in records:
    myRC = Seq.reverse_complement(record.seq)
    if record.seq == myRC:
        hitNbr += 1
    #print(">%s\n%s" %(record.id, record.seq))
print(hitNbr)
