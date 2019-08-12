k= int(input())
j = 0
for i in range(k):
    l=list(map(int, input().strip().split(" ")))
    if l[1]-l[0] >= 2:
        j = j+1

print (j)
