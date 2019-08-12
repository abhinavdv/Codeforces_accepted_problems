n = int(input())
k = []
c = 0
for i in range(n):
    k.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if (k[i][0] == k[j][1]):
            c =c+1
print(c)
        
