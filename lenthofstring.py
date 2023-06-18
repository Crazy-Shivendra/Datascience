a=input("enter\n")
w=s=e=0
for i in a:
    if(i.isdigit()):
        w=w+1
    elif(i.isalpha()):
        s+=1
    else:
        e+=1
print("the no. of digit is",w)   
print("the no. of alphabet is",s)   
print("the no. of special character is",e)   
    