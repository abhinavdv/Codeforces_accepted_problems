k = int(input())
l=0
for i in range (k):
    m=input()
    if m.count("+")==2:
        l=l+1
    else:
        l=l-1
        
print(l)
