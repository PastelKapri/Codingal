sp = int(input("Enter the selling price of the item: "))
cp = int(input("Enter the cost price of the item: "))

if sp > cp:
    print("You have a profit of \n", sp-cp)
else:
    print("You have a loss of \n", "-",cp-sp)