l=int(input())
l=l+1
h = 0
while(h == 0):
    if len(str(l)) != len(set(str(l))):
        l=l+1
    else:
        h= h+1

print(l)
