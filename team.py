
l = int(input())
e = 0
for i in range (l):
    k=list(map(int, input().strip().split(" ")))
    if k[0]+k[1]+k[2]>=2:
        e=e+1

print(e)
        
        

