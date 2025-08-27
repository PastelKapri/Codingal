converter = input("Type 'b' to convert Decimal → Binary, or 'd' to convert Binary → Decimal: ")

def dec_to_bi(n):
    binum = "" 
    while n > 0: 
        binum = str(n % 2) + binum
        n //= 2
    return binum

def bi_to_dec(b):
    res = 0
    for digit in b:
        res = res * 2 + int(digit)
    return res

if converter == 'b':
    dec = int(input("Enter a decimal number: "))
    print(f"The binary value of {dec} is {dec_to_bi(dec)}")

elif converter == 'd':
    bi = input("Enter a binaary number: ")
    print(f"The decimal value of {bi} is {bi_to_dec(bi)}")

else:
    print("Invalid choice. Please enter 'b' or 'd'.")
