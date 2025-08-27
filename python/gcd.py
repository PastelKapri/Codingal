numlarge = int(input("Enter the largest number: "))
numsmol = int(input("Enter the smallest number: "))

while(numsmol):
    numstore = numsmol
    numsmol = numlarge % numsmol
    numlarge = numstore
print("The GCD is", numlarge)