#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*-


compteur = 1
#infile = open('test.txt', 'r')
infile = open('rosalind_ini5.txt', 'r')
outfile = open('outfile.txt', 'w')
myFile = infile.readlines()
for line in myFile:
    if compteur % 2 == 0:
        print(line, end='')
        outfile.write(line)
    compteur += 1
infile.close()
#print(infile.closed)

