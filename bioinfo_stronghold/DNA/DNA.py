a = c = g = t = 0
f=open('DNA.txt', 'r')
f=f.read()
for letter in f.strip():
    if(letter.upper() == "A"):
        a+=1
    elif(letter.upper() == "C"):
        c+=1
    elif(letter.upper() == "G"):
        g+=1
    elif(letter.upper() == "T"):
        t+=1

print(a,c,g,t)

