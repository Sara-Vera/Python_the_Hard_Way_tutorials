

# Practice with strings and text
# Use double and single quotes to denote strings
# Put multiple variables in parentheses separated by commas
# I think you have to define anything used with '%s', right?

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

###############
# To use %s, you need to define variables, or use quotes to define a string at end of line

# Variables Defined .... OR ....
milk = "milk"
eggs = "eggs"
bread = "chickens"

a = "I want %s, %s, and %s." % (milk, eggs, bread)
print a

# .... String definition
c = "I want %s and %s." % ('milk', 'eggs')
print c


# Using %r causes quotation marks around your variables in your output.
b = "I want %r, %r, and %r." % (milk, eggs, bread)
print b

# %r is used for debugging because it displays the raw data of the variable, but %s is used for displaying to users

