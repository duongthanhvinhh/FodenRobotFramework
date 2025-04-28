file = open('./data/text.txt')
file.close()

# With line 1 and 2 above, we need to write file.close() to close the file
# There is another way to close the file automatically, replace 2 lines above by one line below
with(open('./data/text.txt', 'r')) as reader: # Open the file in read mode
    content = reader.readlines() # Output: ['cat\n', 'dog\n', 'fish\n', 'cow\n', 'bird']
    content.reverse()
    with(open('./data/text.txt', 'w')) as writer: # Open the file in write mode
        for line in content:
            writer.write(line)

# Example above: (1) Read all content line by line of the text file and store in a list -> (2) reverse that list -> (3) write the list after being reversed to the file