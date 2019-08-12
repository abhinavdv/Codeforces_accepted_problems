
k=list(map(int, input().strip().split("+")))
k.sort()
k = map(str, k)
m = "+".join(k)
print(m)
