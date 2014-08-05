# %r should only be used for debugging since it gives the 'raw programmers' version of the variable

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
	    "I had this thing",
	    "That you could type up right",
	    "But it didn't sing",
	    "So I said goodnight."
)

## Lesson 9

# \n means 'new line'. Can't be used with %r
days = "Mon Tue WEd Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\n"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes. We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""