l=list(map(int, input().strip().split(" ")))
k=input()
m = k.count("BG")
print(m)
t = 1
h = []
while(t<=l[1]):
    t = t+1
    h.append(k.index("BG"))
    for i in range (m-1):
        h.append(k[int(h[i]+1):].index("BG"))
        
    for i in range(len(h)):
        a = k[int(h[i])]
        k[int(h[i])] == k[int(h[i])+1]
        k[int(h[i])+1] == a
print(h)
print(a)
print(k)
        
