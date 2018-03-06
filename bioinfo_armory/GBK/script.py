#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

from Bio import Entrez

### Best way to read a 3-lines file:
## genus, start, end = open('GBK.txt').read().split('\n')

f=open('rosalind_gbk.txt', 'r')
temp = (f.read().rstrip('\n'))
requestId = temp.split()

## Anthoxanthum[Organism] AND "2003/7/25"[Publication Date] : "2005/12/27"[Publication Date]
myRequet = requestId[0]+'[Organism] AND "'+requestId[1]+'"[Publication Date] : "'+requestId[2]+'"[Publication Date]'

Entrez.email = "damien.courtine@univ-brest.fr"
#handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
#handle = Entrez.esearch(db="nucleotide", term='Anthoxanthum[Organism] AND "2003/7/25"[Publication Date] : "2005/12/27"[Publication Date]')
handle = Entrez.esearch(db="nucleotide", term=myRequet)
record = Entrez.read(handle)
print(record["Count"])

