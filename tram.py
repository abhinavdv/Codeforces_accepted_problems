l=int(input())
a=0
b=0

for i in range (l):
    j=list(map(int, input().strip().split(" ")))
    a = a- j[0]
    a = a+ j[1]
    if a>b:
        b = a
print(b)
    
