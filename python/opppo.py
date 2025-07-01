with open("text.txt","w") as file:
    file.write("this is test")
file.close()

with open("text.txt","r") as file:
    content = file.readlines()
    print("printing words...")
    for line in content:
        print(line.split())
file.close()