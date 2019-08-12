k = list(map(int, input().strip().split(" ")))
h=k[0]
l = 0
for i in range(k[2]):
    l = l + h
    h = h + k[0]
if k[1]<=l:
    print(l-k[1])
else:
    print(0)
