#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
import sys
import os
from Bio import Seq

f = open("rosalind_prot.txt", "r")
line = f.read().rstrip('\n')
print(Seq.translate(line, stop_symbol=''))

#for i in range(0,len(f),3):
#    print(f[i:i+3])
f.close()


