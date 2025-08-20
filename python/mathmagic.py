'''number = int(input("Enter a number: "))

digits = len(str(number))

resultnum = 0

temp = number
while temp > 0:
    digits = temp % 10
    resultnum += digits ** digits
    temp //= 10

if resultnum == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number") '''

'''def romantonum(romaninput):
    roman = {"M":1000, "C":100, "L":50, "X":10, "V":5, "I":1}

    resutlint = 0

    for i in range(len(romaninput)-1):
        if roman[romaninput[i]] < roman[romaninput[i +1]]:
            resutlint -= roman[romaninput[i]]
        else:
            resutlint += roman[romaninput[i]]
    resutlint += roman[romaninput[-1]]
    return resutlint

roman = input("Enter a Roman numeral: ").upper()
print(f"The integer value of {roman} is {romantonum(roman)}")'''

def factors(num):
    print("the factors of", num, "are:")
    for i in range(1, num +1):
        if num % i == 0:
            print(i)
num = int(input("Enter a number to find its factors: "))
factors(num)