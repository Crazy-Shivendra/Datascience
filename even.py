s=e=0
for i in range (10,21):
    if(i%2==0):
        print(i,"is even")
        s+=i
    else:
        e+=i
print("the total sum of even is",s)
print("the total sum of odd is",e)