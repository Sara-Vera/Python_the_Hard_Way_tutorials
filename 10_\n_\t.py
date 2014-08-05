tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\a* Whatever
\b* Whatever\"\nnewline
\r* Carriage Return
\v *What's vertical tab?
\000 Null
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# while True:
  #  for i in ["/","-","|","\\","|"]:
   #     print "%s\r" % i,

x = "There are %d\" types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s\" and those who %s." % (binary, do_not)

print x
print y