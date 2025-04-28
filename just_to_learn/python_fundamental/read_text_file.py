file = open('data/text.txt')

# Read the first 5 characters in the text file
# print(file.read(5))

# Read all the contents of the file
# print(file.read())

# Read the file line by line
# print(file.readline()) # will print the first line in the text file
# print(file.readline()) # will print the second line in the text file

# Print line by line using readline() method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()


# Using readlines to do something
for line in file.readlines():
    print(line)

file.close()