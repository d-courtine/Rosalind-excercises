#!/usr/bin/env python3

import sys
########### Function ###########

def expected_offspring(list_genotype):
    """Compute the expected number of offspeings with dominant genotype.
    Hd = Homozygote dominant; Hr = Homozygote recessive; ht = Heterozygous.
    Probabilities: HdHd = 1; Hdht = 1, HdHr = 1, htht = 0.75, htHr = 0.5,
    HrHr = 0
    """
    freqdom = 0
    for i in range(0,len(list_genotype)):
        if i <= 2:
            freqdom += list_genotype[i]
        elif i == 3:
            freqdom += list_genotype[i]*0.75
        elif i == 4:
            freqdom += list_genotype[i]*0.5
        elif i == 5:
            freqdom += list_genotype[i]*0

    #Return the result times 2 because each couple has 2 offsprings
    return freqdom*2

############# Test #############

test_list = [1, 0, 0, 1, 0, 1]
#print(expected_offspring(test_list))

############# Main #############

infile = 'rosalind_iev.txt'
data = open(infile, 'r')

couple_list = next(data)
couple_list = couple_list.rstrip().split()

correct_list = list()
for elt in couple_list:
    correct_list.append(int(elt))

print(correct_list)


print(expected_offspring(correct_list))





