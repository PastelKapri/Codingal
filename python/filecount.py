file = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/file.txt")
counter = 0
content = file.read()
content_list = content.split("\n")
for l in content_list:
    if l.strip():
        counter += 1
file.close()
print(f"The number of lines in the file is: {counter}")