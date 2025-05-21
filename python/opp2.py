type =int(input("Enter amount to withdraw: "))
note1 = type // 100
note2 = (type % 100) // 50
note3 = (type % 100 % 50) // 10

print("100 notes: ", note1)
print("50 notes: ", note2)
print("10 notes: ", note3)
