k=list(map(int, input().strip().split(" ")))
m = 0
l=list(map(int, input().strip().split(" ")))
for i in l:
           if i>=l[k[1]-1] and i!=0:
               m=m+1
           
print(m)
