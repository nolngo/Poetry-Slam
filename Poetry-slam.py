filename = "poem.txt"
def get_file_lines(filename):
    read_poem = open(filename, 'r')
    return read_poem.readlines()        #this function has outputted a list version of the text file! We can now reference it in following functions
#print(get_file_lines(filename))     #this is to test the return output of the get_file_lines

print("\u0332".join("THIS IS THE POEM BACKWARDS"))      #used the unicode \u0332 to underline the following text, the following text is the intro to the function.
def lines_printed_backwards(lines_list):
    lines_list = lines_list[::-1]       #modified line_list to read backwards using a slice
    for line in lines_list:         #putting the print into a for loop allows the list to be printed in a nicer format, line by line
        print(line)

lines_printed_backwards(get_file_lines(filename))       #this is to call the backwards print function using the return of the original function as the parameter


print("\u0332".join("THIS IS THE POEM IN RANDOM ORDER"))        #used the unicode \u0332 to underline the following text, the following text is the intro to the function.
import random                       #imports the random libraries from python and allows random functions in our program
def lines_printed_random(lines_list):
    random.shuffle(lines_list)      #random.shuffle preserves the amount of lines in the original list and does not introduce repeated lines
    for line in lines_list:         #putting the print into a for loop allows the list to be printed in a nicer format, line by line
       print(line)

lines_printed_random(get_file_lines(filename))


print("\u0332".join("THIS IS THE POEM IN CUSTOM ORDER"))        #used the unicode \u0332 to underline the following text, the following text is the intro to the function.
def lines_printed_custom(lines_list):
    print("These lines begin with B or T or N")      #this for loop will identify and print only list items starting with B, T, or N
    for line in lines_list:
        if line[0] == "B" or line[0] == "T" or line[0] == "N":
            print(line)
    print("These lines do not begin with B or T or N")       #this for look is much like an else function except i wanted to put a space in between them and put the message
    for line in lines_list:
        if line[0] != "B" or line[0] != "T" or line[0] != "N":
            print(line)
lines_printed_custom(get_file_lines(filename))

