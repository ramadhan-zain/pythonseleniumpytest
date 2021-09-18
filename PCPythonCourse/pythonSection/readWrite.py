file = open("test.txt")

# print(file.read())
# print(file.read(3))
# read one single line at a time readline()
# print(file.readline())
# print(file.readline())

# print line by line using readline method

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# lines = file.readlines()
# print(lines)

for line in file.readlines():
    print(line)

file.close()