s = 0
a = int(input("enter the no."))
while (a != 0):
    d = a % 10
    s = s+d
    a = a//10
print(s)
