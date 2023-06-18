s=e=0
a=input('enter the string\n')
for i in a:
    if(i.isupper()):
        s+=1
    elif(i.islower()):
        e+=1
print("the no. of upper case is",s)
print("the no. of lowercase is",e)