#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
import sys
import os

f = open("rosalind_hamm.txt", "r")
seqs = []
for line in f:
    line = line.rstrip('\n')
#    print(line)
    seqs.append(line)
f.close()

seq1 = list(seqs[0])
seq2 = list(seqs[1])
countDiff = 0
for i in range(0,len(seq1)):
    if seq1[i] != seq2[i]:
        countDiff += 1

print(countDiff)

