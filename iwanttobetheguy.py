a = int(input())
l = list(map(int, input().split()))
k= list(map(int, input().split()))
m=l[1:]+k[1:]
m = set(m)
n=0
c=sum(m)
for i in range (a+1):
    n=n+i
if n==c:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

