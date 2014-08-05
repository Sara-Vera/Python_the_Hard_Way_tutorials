print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = int(raw_input())

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Run this script in Terminal and answer the prompts
# Will return your answers

# raw_input treats everything like a string
# input() tries to convert things as if they were Python code but it has security problems, so avoid it
# int(raw_input()) changes it to a integer so you can do math


print 'What\'s your favorite color?',
color = raw_input()

print 'Let me get this right. Your favorite color is %r?' % color

print 'What is your total?',
total = age + weight
print total