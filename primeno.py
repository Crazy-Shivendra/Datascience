s=0
a=int(input("enter the no."))

for i in range(1,a+1):
     if(a%i==0):
        s+=1
    
if(s==2 ):
    print("it is a prime no.")
else:
    print("not a prime no.")

#method 2
if(a==1):
    print(("not a prime no."))
else:
    for i in range(2,a):
      if(a%i==0):
        print("not a prime no.")
        break
    else:
      print("prime no.")
