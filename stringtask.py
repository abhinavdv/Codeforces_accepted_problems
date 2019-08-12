k=input()
k=k.lower()
l=[]
for i in range (len(k)-1):
	if (k[i]!="a" or k[i]!="e"or k[i]!="i" or k[i]!="o" or k[i]!="u" or k[i]!="y"
		l.append('.'+k[i])
print("".join(l))
