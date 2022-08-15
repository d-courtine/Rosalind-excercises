#!/usr/bin/env python3

from Bio import SeqIO

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format. (MULTILINE!!!)

Return: A consensus string and profile matrix for the collection.
If several possible consensus strings exist, then you may return any one of
them.
"""

# records = SeqIO.parse("data.txt", "fasta")
records = SeqIO.parse("rosalind_cons.txt", "fasta")
seqs = list()
size = None

for record in records:
    if not size:
        size = len(record.seq)
    elif size != len(record.seq):
        raise Exception("The protein %s has a different size than the previous"
                        % record.id, "ones! %s vs %s" % (size, len(record.seq))
                        )

    seqs.append(str(record.seq).upper())

# Opposite dictd with letter associated to positions
k = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
m = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
l_list = ['A', 'C', 'G', 'T']

# Iterate over all sequences, position after position
profile = list()
for i in range(0, size):
    pos = [0, 0, 0, 0]  # to record the letters of the current pos; A/T/C/G
    for j in range(0, len(seqs)):
        for letter in l_list:
            if seqs[j][i] == letter:
                pos[k[letter]] += 1

    profile.append(pos)

# Browse the profile to print the consensus
cons = ''
for pos in profile:
    # 'pos' is a list of size 4
    max = 0
    letter = ''

    # Search the most important letter at this position
    for j in range(0, len(pos)):
        if pos[j] > max:
            max = pos[j]
            letter = m[j]
    cons += letter

# Print the consensus and the matrix
print(cons)

for letter in l_list:
    print("%s:" % letter, end='')
    for pos in profile:
        print(" %s" % pos[k[letter]], end="")

    print()

