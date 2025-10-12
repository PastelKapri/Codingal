'''def flips(num1,num2):
    flip = 0
    while(num1>0 or num2>0):
        t1=num1&1
        t2=num2&1
        if t1 != t2:
            flip+=1
        num1>>=1
        num2>>=1
    return flip
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Number of bits to be flipped to convert {num1} to {num2} is {flips(num1,num2)}")'''

import math
def printpowersets(set,setsize):
    powersetsize=(int)(math.pow(2,setsize))
    for outer in range (0,setsize):
        for inner in range (0,setsize):
            if outer & (1<<inner):
                print(set[inner],end="")
        print()
size = int(input("Enter the size of the set: "))
set = []
for i in range(0,size):
    n= int(input("Enter element: "))
    set.append(n)
printpowersets(set, len(set))