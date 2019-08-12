x = int(input())
k=list(map(int, input().strip().split(" ")))
maxx=0
a=0
for i in range(x-1):
    if k[i] <= k[i+1]:
        a=a+1
    else:
        a=0
    if a>maxx:
        maxx=a
print(maxx+1)
