file = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/text.txt", "r")
file2 = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/text2.txt", "w")

for line in file.readlines():
    if not (line.startswith("hi")):
        print(line)

        file2.write(line)
file.close()
file2.close()