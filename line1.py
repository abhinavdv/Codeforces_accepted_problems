l=list(map(int, input().strip().split(" ")))
a = input()
for i in range(l[1]):
    a = a.replace("BG", "GB")
print(a)
