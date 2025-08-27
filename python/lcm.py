def gcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"The LCM of {a} and {b} is {lcm(a, b)}")
        