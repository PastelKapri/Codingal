import os
if os.path.exists("text_new.txt"):
    print("File exists")
    os.remove("text_new.txt")
else:
    file_content = input("Type anything to add a new line to the file: ")
    file_a = open("text_new.txt", "a")
    file_a.write(file_content + "\n")
    file_a.close()

file_new = open("text_new.txt", "x")
file_new.close()