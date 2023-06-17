a=float(input("enter your weight in kg"))
b=float(input("enter your height in m"))
c=a/(b**2)
if(c<18.5):
    print(("you health satus is underweight"))
elif(c>18.5 and c<24.9):
    print(("you health satus is normal"))
elif(c>25 and c<29.9):
    print(("you health satus is overweight"))
else:
    print("your health satus is obese")