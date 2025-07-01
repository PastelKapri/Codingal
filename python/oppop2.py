file_new = open("text4.txt","x")
file_new.close()

import os
if os.path.exists("text04.txt"):
    print("file exists")
    os.remove("text04.txt")
else:
    print("file not exist")
    file = open("text3.txt","w")
    file.write("this is a new file")
    file.close()
    os.remove("text3.txt")

    os.rmdir("test")

