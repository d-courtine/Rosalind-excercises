#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO
 
f = open('rosalind_phre.txt', 'r')
first_line = f.readline().rstrip()

records = SeqIO.parse(f, 'fastq')
numSeqReject = 0
for record in records:
    summ  = 0
    for i in record.letter_annotations["phred_quality"]:
        summ += i
    mean = summ/len(record.letter_annotations["phred_quality"])
    if int(first_line) > mean:
        numSeqReject += 1
print(numSeqReject)
