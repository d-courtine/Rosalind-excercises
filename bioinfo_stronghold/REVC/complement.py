from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

f=open('complement.txt', 'r')
f=f.read()
f=f.upper()
my_seq = Seq(f.strip(), generic_dna)

print(my_seq.reverse_complement())

