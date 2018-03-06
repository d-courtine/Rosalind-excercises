#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

# k homozygous dominant
# m heterozygous recessive
# n homozygous recessive

#### Better solution from Rosalind
#def firstLaw(k,m,n):
#    N = float(k+m+n)
#    return 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) )
####


k, m, n = 20, 21, 23

''' Probability two random organisms mate and produce individual
with a dominant allele'''
# Transform <int> in <float>
k,m,n = map(float, (k,m,n))

total = k+m+n
pk = k/total
pm = m/total
pn = n/total

# Max probability
prob = 1

# subtract probability if both homozygous recessive
prob -= pn*((n-1)/(total-1))

# subtract prob if one homozygous recessive & one heterozygous recessive
# double because two scenarios (e.g. Aa * aa & aa * Aa)
prob -= 2*pn*(m/(total-1))*0.5

# subtract prob if both heterozygous recessive
prob -= pm*((m-1)/(total-1))*0.25
print(prob)


###'''Also possible to accomplish by calculating the dominant
###allele probabilities instead'''
###
###def prob_dom_alleles(k,m,n):
###    k,m,n = map(float, (k,m,n))
###    t = k+m+n
###
###    # Simply add up probabilities of possessing dominant allele
###    # AA x anything
###    prob = k/t
###    
###    # Aa x AA
###    prob += pm*(k/(t-1))
###    
###    # Aa x Aa
###    prob += pm*((m-1)/(t-1))*.75)
###    
###    # Aa x aa & aa x Aa
###    prob += 2*pm*(n/(t-1)*.5))
###    
###    # aa x AA
###    prob += pn*(k/(t-1))
###return prob




