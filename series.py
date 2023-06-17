w = 1
j = 0
a = int(input("enter the range\n"))
for i in range(1, a+1):
    w *= i
    e = 1/w
    j += e
print(j)
