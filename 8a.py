a=input()
b=input()
c=input()
m=0
n=0
if (a.find(b)!= -1 and a.find(c)!= -1):
	k=a.index(b)
	l=a.index(c)
	if k<l:
		m=m+1
	rev = a[::-1]
	o=rev.index(b)
	p=rev.index(c)
	if o<p:
		n=n+1
else:
	print("fantasy")

if m!=0 and n==1:
	print("both")
elif m==0 and n==1:
	print("backward")	
elif m==0 and n==1:
	print("forward")	
