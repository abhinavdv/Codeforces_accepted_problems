k = int(input())
m = list(map(int, input().split()))
h = m[0]%2
g = m[1]%2
f = m[2]%2
l = 0
for i in range(k):
    if h+g+f<2:
        if m[i]%2!=0:
            l=i+1
            break
    else:
        if m[i]%2==0:
            l=i+1
            break

print(l)
        
        
