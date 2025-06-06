alpha = str(input("Enter any character and i'll check if it's part of the alphabet: "))
if alpha.isalpha():
    print(f"Yes, {alpha} is part of the alphabet.")
else:
    print(f"No, {alpha} is not part of the alphabet.")