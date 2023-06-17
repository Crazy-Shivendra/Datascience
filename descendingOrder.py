num1,num2,num3=int(input()),int(input()),int(input())
if(num1>num2):
    if(num2>num3):
        print(num1)
    elif(num3>num2):
        print(num1)
elif(num2>num3):
    if(num3>num1):
        print(num2)
    elif(num3<num1):
        print(num2)
else:
    if(num2<num1):
        print(num1)
    elif(num2<num):
        print(num1)


       