# argv is argument variable
# the following code 'unpacks' the argv into 4 variables that are assigned
# It says 'Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.'

# sys is basically a system of features you want to use. Called a "Module"

from sys import argv

script, first, second, third = argv

print 'The script is called:', script
print 'Your first variable is:', first
print 'Your second variable is:', second
print 'Your third variable is:', third

# In Terminal
# saravera:Desktop saravera$ python 13_Parameters_Unpacking.py stuff things that
# Returns:
# The script is called: 13_Parameters_Unpacking.py
# Your first variable is: stuff
# Your second variable is: things
# Your third variable is: that
# saravera:Desktop saravera$

# Add a raw_input for fun
city = raw_input('Where do you live? ')

print 'So you live in %r? Right on!' % city