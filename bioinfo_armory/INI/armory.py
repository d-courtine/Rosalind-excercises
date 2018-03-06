#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio.Seq import Seq

f=open('rosalind_ini.txt', 'r')
readSeq = f.read().rstrip('\n')
mySeq = Seq(readSeq)

tab = ['A', 'C', 'G', 'T']
for i in tab:
    print(mySeq.count(i), end=' ')

print('')
