h = float(input("Enter height in centimeters: "))
w = float(input("Enter weight in kilograms: "))
bmi = w / (h / 100) ** 2
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You have a normal weight.")
elif bmi <= 29.9:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You are obese.")
elif bmi >= 39.9:
    print("You are very obese.")
else:
    print("You are extremely obese.")