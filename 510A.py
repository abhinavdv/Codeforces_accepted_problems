a,b = list(map(int, input().split()))
a = int(a)
b = int(b)
for i in range(1,a+1):
    if i%2!=0:
        for j in range(0,b):
            print("#", end='')
        print(end="\n")
    else:
        if i%4!=0:
            for j in range(0,b-1):
                print('.', end = "")
            print('#', end = '')
            print(end="\n")
        else:
            print('#', end='')
            for j in range(0,b-1):
                print('.', end = '')
            print(end = '\n')
                
    
