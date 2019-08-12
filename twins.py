n = input()
k = list(map(int, input().strip().split(" ")))
c = 0
k.sort()
p1 = 0
p2 = 0
while (p1<= p2):
    p1 = p1 + max(k)
    k.remove(max(k))
    p2 = sum(k)
    c = c + 1

print (c)
    
    
