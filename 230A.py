from operator import itemgetter
a,b = input().strip().split()
a = int(a)
b = int(b)
k=0
dict = {0:0}
l =[]
for i in range(0,b):
    m = list(map(int, input().split()))
    l.append(m)
l.sort(key= lambda x : x[0])

for i in range(0,b):
     if a>l[i][0]:
         a+=l[i][1]
     else:
         print("NO")
         k=1
         break
if(k==0):
     print("YES") 