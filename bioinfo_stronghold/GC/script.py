#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
import sys
import os
import re
from Bio import SeqIO
from Bio import SeqUtils

#records = list(SeqIO.parse("test.txt", "fasta"))
first = True
trackSeq = ["", ""]  #Keep a trace of the previous seq: defline | G+C content
highest = ["", ""]  #Keep a trace of the seq with the highest G+C content: defline | G+C content

for seq_record in SeqIO.parse("rosalind_gc.txt", "fasta"):
#    print(seq_record.id)    #fasta Defline!
#    print(seq_record.seq)   #fasta Sequence
#    print(len(seq_record)) 
#    print("G+C:", SeqUtils.GC(seq_record.seq))
    #print(seq_record.seq.alphabet)
    if first:
        trackSeq[0] = seq_record.id
        trackSeq[1] = SeqUtils.GC(seq_record.seq)
        first = False
    else:
        #if the current G+C is higher than the previous, keep the current sequence
        gc_cont = SeqUtils.GC(seq_record.seq)
        if trackSeq[1] < gc_cont: 
            trackSeq[0] = seq_record.id
            trackSeq[1] = gc_cont

for item in trackSeq:
    print(item)









