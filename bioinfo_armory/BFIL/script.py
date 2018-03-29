#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import SeqIO
from Bio.SeqIO import QualityIO
from Bio.Seq import Seq

f = open('rosalind_bfil.txt', 'r')
#f = open('test.txt', 'r')
threshold = f.readline().rstrip()
threshold = int(threshold)

####
# 
# Use SeqIO.QualityIO._get_sanger_quality_str(record/subrecord) 
# http://biopython.org/DIST/docs/api/Bio.SeqIO.QualityIO-module.html#_get_phred_quality
#
# IMPORTANT: scan for positions striclty LOWER than the given threshold !!!
#
####
#print(threshold)
#print()

records = SeqIO.parse(f, 'fastq')

for record in records:
    first = True
    head_trim = 0
    tail_trim = 0
    
    # Tester chaque positions
    for i in range (0, len(record.letter_annotations['phred_quality'])):
        # Tester le début
        if first == True:
            # Tester si le début est inferieur
            if record.letter_annotations['phred_quality'][i] < threshold:
                # Garder la dernière position qui est inférieur au seuil (garder first == True)
                # Ajouter le offset de 1, car 0 == 1ere position
                head_trim = i + 1
            # Si la position est supérieur, on ne considère plus que c'est le début
            else:
                first = False

        # Tester les autres positions
        else:
            # Tester si la position est inf au seuil
            if record.letter_annotations['phred_quality'][i] < threshold:
                # garder le début de la partie à trimmer
                if tail_trim == 0:
                    tail_trim = i
            else:
                tail_trim = 0

    if tail_trim == 0:
        subrecord = record[head_trim : ]
    else:
        subrecord = record[head_trim : tail_trim]

#    print("head: %s\ttail: %s" %(head_trim, tail_trim))


    print("@%s" % subrecord.id)
    print(subrecord.seq)
#    print(record.letter_annotations['phred_quality'])
#    print(subrecord.letter_annotations['phred_quality'])
    print("+")
    for i in subrecord.letter_annotations['phred_quality']:
        print(QualityIO._phred_to_sanger_quality_str[i], sep = "", end = "")
    print()

f.close()
