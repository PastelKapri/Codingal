temp = int(input("Enter the temperature in Celsius: "))
if temp < 15 and temp >= 0:
    print("It's cold")
elif temp >=15 and temp < 21:
    print("It's mild")
elif temp >= 21 and temp < 28:
    print("It's warm")
elif temp >= 28 and temp < 35:
    print("It's hot")
elif temp >= 35:
    print("It's very hot")
elif temp < 0 and temp >= -20:
    print("It's freezing")
elif temp >= -272 and temp < -89:
    print("Wait, is that even possible?")
