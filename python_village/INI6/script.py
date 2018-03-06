#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*-

#infile = open('test.txt', 'r')
infile = open('rosalind_ini6.txt', 'r')

myFile = infile.readlines()
for line in myFile:
    words = line.split()
#    print(words)
infile.close()

myDict = {}
for word in words:
    if word in myDict:
        myDict[word] += 1
    else:
        myDict[word] = 1

for cle,val in myDict.items():
    print("{}\t{}" .format(cle,val))


