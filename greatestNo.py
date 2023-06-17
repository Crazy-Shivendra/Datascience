#wap to input 3 no. and  find largest one
a=int(input("enter your no 1."))
b=int(input("enter your no 2.\n"))
c=int(input("enter your no 3.\n"))
if(a>b and a>c):
    print ("Number 1 is greatest")
elif(b>a and b>c):
    print ("Number 2 is greatest")
else:
    print ("Number 3 is greatest")