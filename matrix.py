k=[]
for i in range (5):
    k.append(list(map(int, input().strip().split(' '))))
    if (k[i].count(1) == 1):
        r = i
        c = k[i].index(1)
print(abs(r - 2)+abs(c - 2))
