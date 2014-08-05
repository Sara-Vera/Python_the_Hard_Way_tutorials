from sys import argv

# python 20_Functions_Files.py 20_test.txt
script, input_file = argv

# Defining the functions we need
# Prints the entire file
def print_all(f):
  print f.read()

# Go back to the beginning of the file
def rewind(f):
	f.seek(0)

# Print every line separately, but consecutively
def print_a_line(line_count, f):
	print line_count, f.readline()

# Opening the input file from argv "20_test.txt"
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# print the first line and move the next, incremented by 1, could also use current_line += 1 as a contraction of current_line = current_line + 1

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)