def get_file_lines(filename):
    poem = open(filename, 'r')
    return poem.readlines()

filename = "poem.txt"
print(get_file_lines(filename))