s=0
a=int(input("enter the no."))
b=a
while(a!=0):
    d=a%10
    s=s+d**3
    a=a//10
if(b==s):
    print("armstrong no.")
else:
    print("not an armstrong no.")