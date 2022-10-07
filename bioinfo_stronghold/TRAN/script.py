#!/usr/bin/env python3

from Bio import SeqIO

"""
Transition:
    - A <--> G
    - C <--> T

Transversion:
    - A <--> T
    - A <--> C
    - G <--> C
    - G <--> T
"""

def ts_or_tv(a,b):
    """ Test if it is a transition or a transversion.
    The idea is to test for transition (easier). Else it is a transversion

    Return "True" for transition; "False" for transversion
    """
    state = None
    t = [a, b]
    t.sort()

    if t == ['A', 'G']:
        state = True
    elif t == ['C', 'T']:
        state = True
    else:
        state = False
 
    return state


s1, s2 = None, None

# seqs = SeqIO.parse('data.fa', 'fasta')
seqs = SeqIO.parse('rosalind_tran.txt', 'fasta')

for seq in seqs:
    # first sequence goes in "s1", second in "s2"
    if not s1:
        s1 = str(seq.seq).upper()
    else:
        s2 = str(seq.seq).upper()

ts, tv = 0, 0

for i in range(0, len(s1)):
    if s1[i] == s2[i]:
        continue
    else:
        # is it a transition or a transversion?
        if ts_or_tv(s1[i], s2[i]):
            ts += 1
        else:
            tv += 1

print(ts/tv)

