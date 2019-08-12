a = []
for i in range(5):
    a.append(int(input()))
b = []
for i in range(a[4]):
    b.append(1)
for i in range (4):
    for j in range(a[i]-1,len(b),a[i]):
        b[j] = 0
if ((a[0] > a[4]) or (a[1] > a[4]) or (a[2] > a[4]) or (a[3] > a[4])):
        print(0)
else:
        print(b.count(0))
