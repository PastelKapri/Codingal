num = int(input("Enter a number: "))

ognum = num
reversednum = 0

while num > 0:
    dig = num % 10
    reversednum = reversednum * 10 + dig
    num //=10

if ognum == reversednum:
    print(f"{ognum} is a palindrome")
else:
    print(f"{ognum} is not a palindrome")