a = 12
b = 43
c = 12

print(a != b)
print(a != c)

d = "python"
e = "coding"
if d != e:
    print(d ,"not equal to" ,e)

x = int(input("Enter a number: "))
if x%2 !=0:
    print("The number is odd")
else:
    print("The number is even")

r=12
h=32
if (r==12) and (h==32):
    print("Both conditions are true")
else:
    print("At least one condition is false")
if (r==12) or (h==32):
    print("At least one condition is true")
else:   
    print("Both conditions are false")
if not (r==12):
    print("r is not equal to 12")
else:
    print("r is equal to 12")