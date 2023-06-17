#wap to input marks of a student and print their grade according to their marks
a=int(input("enetr your marks"))
if(a>90 and a<=100):
    print(("your grade is A+"))
elif(a>80 and a<=90):
    print("your grade is A")
elif(a>70 and a<=80):
    print("your grade is B+")
elif(a>60 and a<=70):
    print(("your grade is B"))
elif(a>50 and a<=60):
    print(("your grade is C+"))
elif(a>40 and a<=50):
    print(("your grade is C"))
else:
    print("you are fail")