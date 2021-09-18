# with open('test.txt', 'r') as file:

# read te file and store all the lines in list
# reverse the list
# write back the list to the file

with open('test.txt', 'r') as reader:
    content = reader.read().splitlines()  # this will split each line
    content = reversed(content)

    with open('text3.txt', 'w') as writer:
        for line in content:
            writer.write(line + "\n")