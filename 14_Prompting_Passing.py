
# Run this script in the command line. Remember to add args for argv
# The prompt can be any character. We just chose '>' but doesn't matter
# argv is used when you want users to input in the command line
# raw_input is used when you want users to input while the script is running

from sys import argv

script, user_name = argv
prompt = '> '

print 'Hi %s, I\'m the %s script.' % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print 'Where do you live %s?' % user_name
lives = raw_input(prompt)

print 'What kind of computer do you have?'
computer = raw_input(prompt)

print """ Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)