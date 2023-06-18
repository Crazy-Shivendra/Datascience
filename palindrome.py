s=0
a=int(input("enter the no."))
b=a
while(a!=0):
    d=a%10
    s=s*10+d
    a=a//10
if(b==s):
    print("palindrome no.")
else:
    print(("not an palindrome no."))
