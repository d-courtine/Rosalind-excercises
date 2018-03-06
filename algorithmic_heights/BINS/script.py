#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
import sys
import os
import math

###### Read in file

f = open("rosalind_bins.txt", "r")
lines = []
for line in f:
    line = line.rstrip('\n')
    lines.append(line)
f.close()

len_n = int(lines[0])
len_m = int(lines[1])
n = lines[2].split()
n_final = []
for i in n:
    n_final.append(int(i))

#####
m = lines[3].split()
m_final = []
for i in m:
    m_final.append(int(i))

#####
result_arr = []

for i in range(0, len_m):
    key = m_final[i]
    lowIndex = 1
    highIndex = len_n
    
    while lowIndex <= highIndex:
        middleIndex = math.floor((lowIndex + highIndex)/2)
        middleValue = n_final[middleIndex-1]

        if middleValue == key:
            result_arr.append(middleIndex)
            break

        # Discard the upper list: remove from middleIndex to highIndex
        # So keep lowIndex to middleIndex-1
        if middleValue > key:
            highIndex = middleIndex-1

        # Discard the lower list: remove from lowIndex to middleIndex #-1
        # So keep middleindex to highIndex
        else: #middleValue < key
            lowIndex = middleIndex+1

    # Check if a new value was append in the result_arr
    if len(result_arr) == i:
        result_arr.append(-1)
    
for i in range(0, len(result_arr)):
    print(result_arr[i], end=" ")
print("\n", end="")


#recherche_dichotomique_récursive(élément, liste_triée):
#   m = longueur de liste_triée / 2 ;
#   si liste_triée[m] = élément :
#       renvoyer m ;
#   si liste_triée[m] > élément :
#       renvoyer recherche_dichotomique_récursive(élément, liste_triée[1:m]) ;
#   sinon :
#       renvoyer recherche_dichotomique_récursive(élément, liste_triée[m:l]) ;


#Note: assume that list and key are already set
#set lowIndex = 1
#set highIndex = length of list
#repeat until lowIndex is larger than highIndex
#    set middleIndex = (lowIndex + highIndex)/2   round down
#    set middleValue = list[middleIndex]
#    if middleValue == key
#        print "Found at " + middleLocation
#        end program
#
#    Note: We didn't find, it check to see if too high or too low:
#    if middleValue > key then
#        Note: Too high, change the upper bound
#        highIndex = middleLocation - 1
#    else
#        Note: Too low, change the lower bound
#        lowIndex = middleLocation + 1
#
#print "Value not found"
