'''def numsame(num1,num2):
    if ((num1^num2)!=0):
        print("Not same")
    else:
        print("Same")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
numsame(num1,num2)

def oddoccuringnum(arr):
    res = 0
    for element in arr:
        res = res^element
    
    return res
arr = []
n = int(input("Enter the array size: "))
while(n):
    num = int(input("Enter the element: "))
    arr.append(num)
    n -= 1
print(f"The odd occuring number is {oddoccuringnum(arr)}")'''
    
def twoodd(arr,size):
    xorof2 = arr[0]
    x=0
    y=0
    setbit=0
    for i in range (1,size):
        xorof2 = xorof2^arr[i]
    setbit = xorof2 & ~(xorof2-1)
    for i in range(size):
        if(arr[i] & setbit):
            x = x^arr[i]
        else:
            y = y^arr[i]
    print(f"The two odd occuring numbers are {x} and {y}")
arr = []
arr_size = int(input("Enter the array size: "))
for i in range(0,arr_size):
    z=input("enter the element: ")
    arr.append(int(z))
twoodd(arr,arr_size)
