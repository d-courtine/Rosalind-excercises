#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
#from Bio.SeqUtils import ProtParam

aa_dict = {'A' : 71.03711, 'C' : 103.00919, 
    'D' : 115.02694, 'E' : 129.04259,
    'F' : 147.06841, 'G' : 57.02146,
    'H' : 137.05891, 'I' : 113.08406,
    'K' : 128.09496, 'L' : 113.08406,
    'M' : 131.04049, 'N' : 114.04293,
    'P' : 97.05276, 'Q' : 128.05858,
    'R' : 156.10111, 'S' : 87.03203,
    'T' : 101.04768, 'V' : 99.06841,
    'W' : 186.07931, 'Y' : 163.06333 }

#for key, value in aa_dict.items():
# print(key, value)

with open("rosalind_prtm.txt", 'r') as f:
    for line in f:
        seq = line.rstrip()
        #print(seq)
        weight = 0
        for aa in seq:
            weight += aa_dict[aa]
        print("%.3f" % weight)


#with open("test.txt", 'r') as f:
# for line in f:
#  seq = line.rstrip()
#  print(seq)
#  X = ProtParam.ProteinAnalysis(seq)
#  weight = X.molecular_weight()-18.01056
#  print(weight)
