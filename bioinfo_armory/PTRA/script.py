#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import Seq
with open('rosalind_ptra.txt', 'r') as f:
    dnaSeq = f.readline().rstrip()
    protSeq = f.readline().rstrip()

indexTab = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]
indexResult = []

for i in indexTab:
    currSeq = Seq.translate(dnaSeq, to_stop = False, table = i, stop_symbol = '')
    if currSeq == protSeq:
        indexResult.append(i)

for i in indexResult:
    print(i, end=' ')
print('')

