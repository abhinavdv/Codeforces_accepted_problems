
k=0
m=0
l=list(map(int, input().strip().split(" ")))
if (l[0]%l[2]==0):
    k =(l[0]//l[2])
else:
    k =(l[0]//l[2])+1
if (l[1]%l[2]==0):
    m=(l[1]//l[2])
else:
    m=(l[1]//l[2])+1
x=k*m
print(x)
