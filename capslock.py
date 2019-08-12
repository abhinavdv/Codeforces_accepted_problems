a=input()

if(len(a) == 1) and (a.islower() == True ):
    a = a.upper()
    
elif(a.isupper() == True):
    a = a.lower()

elif(a[0].islower() == True) and (a[1:].isupper() == True):
    a = a.capitalize()


print(a)
