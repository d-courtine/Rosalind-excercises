a = c = g = t = 0
f=open('RNA.txt', 'r')
f=f.read()
f=f.upper()
f=f.replace("T", "U")
print(f.strip())

