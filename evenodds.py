n,m=input().split()
n=int(n)
m=int(m) 
if n%2==0:
	if m<=n//2:
		print((2*m)-1) 
	else:
		print((m-(n//2))*2) 
else:
	if m<=((n//2)+1):
		print((2*m)-1) 
	else:
		print(((m-(n//2))-1)*2)
