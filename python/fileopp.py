file = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/text.txt", "r")
text = print(file.read(29))
file.close()

file = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/text.txt", "a")
file.write("This is a new line to the file.\n")
file.close()
