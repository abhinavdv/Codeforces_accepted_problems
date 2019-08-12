l=list(map(int, input().strip().split(" ")))
m=list(map(int, input().strip().split(" ")))
m.sort()
k=99999999999999999999999999999999999999995
for i in range (len(m)-l[0]+1):
    if abs(m[i+l[0]-1]-m[i]) < k:
        k = m[i+l[0]-1] - m[i]
if l[0]<=l[1]:
    print(k)
else:
    print(0)
