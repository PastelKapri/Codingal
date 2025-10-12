def powerof8(num):

    if num <= 0:
        return False
    
    if (num & (num - 1)) != 0:
        return False

    count = 0
    while num > 1:
        num >>= 1  
        count += 1

    return (count % 3 == 0)

num = int(input("Enter a number: "))
if powerof8(num):
    print(f"{num} is a power of 8")
else:
    print(f"{num} is not a power of 8")
