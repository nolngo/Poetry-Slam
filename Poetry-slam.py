filename = "poem.txt"
def get_file_lines(filename):
    poem = open(filename, 'r')
    return poem.readlines()
def lines_printed_backwards(lines_list):
    print(lines_list[::-1])

lines_printed_backwards(get_file_lines(filename))
