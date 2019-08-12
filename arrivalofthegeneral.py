k = int(input())
l = list(map(int, input().split()))
m = l[-1::-1]
if l.index(max(l))>l.index(min(l)):
    print(k-l.index(min(m))
else:
    print(k-1-l.index(min(m)) + l.index(max(m)))
