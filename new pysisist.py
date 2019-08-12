m = int(input())
g = 0
a = 0
b = 0
for i in range (m):
    l=list(map(int, input().strip().split(" ")))
    g = g+l[0]
    a = a+l[1]
    b = b+l[2]

if (g == 0 and a == 0 and b == 0):
    print("YES")
else:
    print("NO")
