
file = open("text file.txt")

# Read all the content of file
# print(file.read())

# Read only one line
line = file.readline()

while line != "":
    print(line)
    line = file.readline()

file.close()
    