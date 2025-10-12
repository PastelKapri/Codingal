num1 = 10
num2 = 4

print("AND Operation: ", num1 & num2)
print("OR operation: ",num1 | num2)
print("NOT operation: ", ~num1)
print("XOR operation: ", num1 ^ num2)
print("Left Shift operation: ", num1 << 2)
print("Right Shift operation: ", num1 >> 2)

def envenorood(num):
    if (num ^ 1 == num + 1):
        return True
    else:
        return False

number = int(input("Enter a number to check even or odd: "))
if envenorood(number):
    print(number, "is even")
else:
    print(number, "is odd")

def noofbits(n):
    count = 0
    while n > 0:
        count += 1
        n >>= 1
    return count
number2 = int(input("Enter a number to find the number of bits: "))
print("Number of bits in", number2, "is", noofbits(number2))