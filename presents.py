n=int(input())
k=list(map(int, input().split()))
l=[]
for i in range(n):
    l.append(k.index(i+1)+1)
print(" ".join(map(str, l)))


