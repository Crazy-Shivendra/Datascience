a=input("enter the string\n")
if(len(a)<2):
    print()
else: 
    s=a[:2]
    f=a[len(a)-2:]
    print(s+f)
