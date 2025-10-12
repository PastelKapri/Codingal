def numofbits(n):
    ones = 0
    zeros = 0
    while(n):
        if (n&1==1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print(f"There are {ones} ones and {zeros} zeros in the binary representation of the number.")

number = int(input("Enter a number to find the number of ones and zeros in its binary representation: "))
numofbits(number)

def setornot(num, n):
    if num & (1<<(n-1)):
        print("Set")
    else:
        print("Not set")

number = int(input("Enter a number: "))
n = int(input("Enter the bit position: "))
setornot(number, n)
