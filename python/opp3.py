math = int(input("enter math score: "))
english = int(input("enter english score: "))
science = int(input("enter science score: "))
french = int(input("enter french score: "))

sum = math + english + science + french
perc = (sum/400)*100
print("Total marks: ", sum)
print("Percentage: ", perc)