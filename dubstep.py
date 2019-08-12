m = list(map(str, input().split("WUB")))
k = m.count("")
if k!=0:
    for i in range(k):
        m.remove("")
print(" ".join(m))
