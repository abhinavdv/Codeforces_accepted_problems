k = int(input())

l=list(map(int,input().split()))
sum = 0
for i in range(k):
	sum+=l[i]
print(sum/k)