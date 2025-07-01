file_read = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/file.txt")
print(file_read.read())

file_write = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/file.txt", "w")
file_write.write("This is a new line to the file.\n")

file_append = open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/file.txt", "a")
file_append.write("This line is appended to the file.\n new line added.\n new line added.\n")

