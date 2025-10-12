def power2(number):
    if number == 0:
        return 0
    if ((number & (~(number-1)))==number):
        return 1
    return 0
number = int(input("Enter a number: "))
if power2(number):
    print(f"{number} is a power of 2")
else:
    print(f"{number} is not a power of 2")

def computpower(x,y):
    res = 1
    while y>0:
        if (y%2==0):
            x=x*x
            y>>=1
        else:
            res = res*x
            y-=1
    return res
x = int(input("Enter the base: "))
y = int(input("Enter the exponent: "))
print(f"{x} raised to the power {y} is {computpower(x,y)}")

def powerof4(num):
    count=0
    if num<=0:
        return False
    if (num & (num-1))!=0:
        return False
    while(num>1):
        num>>=1
        count+=1
    return (count%2==0)
num = int(input("Enter a number: "))
if powerof4(num):
    print(f"{num} is a power of 4")
else:
    print(f"{num} is not a power of 4")