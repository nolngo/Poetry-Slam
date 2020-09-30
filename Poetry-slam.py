filename = "poem.txt"
def get_file_lines(filename):
    read_poem = open(filename, 'r')
    return read_poem.readlines()

print(get_file_lines(filename))     #this is to test the return output of the get_file_lines

def lines_printed_backwards(lines_list):
    lines_list = lines_list[::-1]
    for line in lines_list:
        print(line)


lines_printed_backwards(get_file_lines(filename))       #this is to call the backwards print function using the return of the original function as the parameter

import random
def lines_printed_random(lines_list):
    random.shuffle(lines_list)      #random.shuffle preserves the amount of lines in the original list and does not introduce repeated lines
    for line in lines_list:
       print(line)

lines_printed_random(get_file_lines(filename))

def lines_printed_custom(lines_list):
    print("These lines begin with B or T")
    for line in lines_list:
        if line[0] == "B" or line[0] == "T" or line[0] == "N":
            print(line)
    print("These lines do not begin with B")
    for line in lines_list:
        if line[0] != "B" or line[0] != "T" or line[0] != "N":
            print(line)
lines_printed_custom(get_file_lines(filename))