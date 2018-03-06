#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import ExPASy
from Bio import SwissProt

f=open('rosalind_dbpr.txt', 'r')
protId= f.read().rstrip('\n')

handle = ExPASy.get_sprot_raw(protId) #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins
#print(dir(record))
#print(record.cross_references)

for item in record.cross_references:
    if item[0] == 'GO' and item[2][:2] == 'P:':
        #print(item)
        print(item[2][2:])
