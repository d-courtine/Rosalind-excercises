#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
import sys
import os

f = open("rosalind_subs.txt", "r")
lines = []
for line in f:
    line = line.rstrip('\n')
    lines.append(line)
f.close()

seq = list(lines[0])
motif = list(lines[1])

allPos = []
currentPos = ""
# Parcours la séquence lettre par lettre

for i in range(0,len(seq)):
    currentPos = i
    if i > (len(seq)-len(motif)):
        break
    # si lettre courrante = 1ere lettre du motif, check les position suivantes
    if seq[i] == motif[0]:
        # Parcours le motif
        for j in range(1, len(motif)):
            # Si position sequence + j est different de la position j du motif
            if seq[i+j] != motif[j]:
                # Arrête la recherche et on passe a la position suivante de la seq
                break
            """Si on atteint la dernière position du motif, c'est bon
              On garde la position du début du motif sur la séquence
              qui est gardée dans la variable currentPos.
              On la met donc dans la liste contenant toutes les position, allPos """
            if j == (len(motif)-1):
                allPos.append(currentPos+1)

for i in allPos:
    print(i, end=' ')
print("\n", end = '')
