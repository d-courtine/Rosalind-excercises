#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO
from Bio.SeqIO import QualityIO
from Bio.Seq import Seq

#f = open('rosalind_bfil.txt', 'r')
f = open('test.txt', 'r')
threshold = f.readline().rstrip()
threshold = int(threshold)

# Iterate over FastQ records is string in tuple
#for (title, sequence, quality) in SeqIO.QualityIO.FastqGeneralIterator(f):
#    print(title, sequence, quality)
#    print(SeqIO.read(quality, "qual"))


####
#
# Use SeqIO.QualityIO._get_sanger_quality_str(record/subrecord) 
# http://biopython.org/DIST/docs/api/Bio.SeqIO.QualityIO-module.html#_get_phred_quality
####


records = SeqIO.parse(f, 'fastq')
for record in records:
    subrecord = record[4:15]
    print(subrecord.letter_annotations['phred_quality'])
    for i in subrecord.letter_annotations['phred_quality']:
        print(QualityIO._phred_to_sanger_quality_str[i], sep = "", end = "")
    print()
    print(subrecord)
    print()

f.close()
