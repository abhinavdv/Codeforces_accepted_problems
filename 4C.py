k = int(input())
d = {}
for i in range(k):
    m = input()
    if m not in d:
        d[m] = 1
        print('OK')
    else:
        print(m+str(d[m]))
        d[m] +=1
    