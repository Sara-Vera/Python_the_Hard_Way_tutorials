def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d chesses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man That's enough for a party!"
	print "Get a blanket. \n" # inserts a new line in between function calls

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



def Yosemite(climbing, hiking):
	print "We're climbing %d feet today." % climbing
	print "And we're going to hike %d miles to get there." % hiking

print "Let's do this!"
Yosemite(1000, 7)