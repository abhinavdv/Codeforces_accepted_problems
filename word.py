k = list(map(str, input().strip()))
m=0
l=0
for i in range(len(k)):
    if k[i].isupper():
        l=l+1
    else:
        m=m+1
k = "".join(k)
if m>=l:
    print(k.lower())
else:
    print(k.upper())
