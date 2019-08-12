k = int(input())
n=0
m=0
if k%2==0:
    n=k//2
    m=k//2
else:
    n=k//2
    m=k//2+1
while (iscomposite(m)==False and iscomposite(n)==False):
    n=n-1
    m=m+1

print(chr(m)+" "+chr(n))
