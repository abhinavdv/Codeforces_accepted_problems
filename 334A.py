k = int(input())
t = 0
l = []
for i in range(k):
    l.append(int(input()))
for i in range(k-1):
    if l[i]!=l[i+1]:
        t=t+1
print(t+1)
        
