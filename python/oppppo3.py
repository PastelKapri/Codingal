output_file = open("upd_file.txt","w")
input_file = open("repeat.txt","r")

lssf = set()

for line in input_file:
    if line not in lssf:
        output_file.write(line)
        lssf.add(line)
output_file.close()
input_file.close()
