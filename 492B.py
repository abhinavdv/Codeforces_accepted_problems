a,b = input().strip().split()
a = int(a)
b = int(b)
diff = 0
l = list(map(int, input().split()))
# if l.count(0) == 0:
#     l.append(0)
# if l.count(b) == 0:
#     l.append(b)
l = sorted(l)
for i in range(1,len(l)):
    if(l[i]-l[i-1]>diff):
        diff = l[i]-l[i-1]
q = min(l)
e = b - max(l)
this = max(q,e)
print('{0:.15f}'.format(max(this,diff/2)))
