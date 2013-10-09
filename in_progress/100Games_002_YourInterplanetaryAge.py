#
#               	100 Games Project 
#
#	See http://mousesmusings.blogspot.co.uk/search/label/100%20Games for more information
#	Inspired by Jennifer Dewalt's 180 websites in 180 days - http://jenniferdewalt.com/
#
#
# 				Game #002: Your Interplanetary Age
#
# 	1. Ask the user's age
#	2. Return their age in days and years of each of the planets
#	3. Extra credit: Format the results in a nice table, probably | pipe | delimited 
#	4. Extra extra credit: Get the welcome message to print out like a videprinter	
#
#	Thanks to http://www.exploratorium.edu/ronh/age/ for the information on 
#	the orbits of the planets in Earth days
#
# 	Inspired by Jennifer Dewalt's 180 websites in 180 days
# 	http://jenniferdewalt.com/
#
###############################################################################
import time

print ("Hello again! Welcome to the next game in the 100 Games Project")
print ("This time we're going to calculate your age in days and years on other planets in the solar system")
time.sleep(1)

print("What is your age?")
age = int(input(">>> "))



time.sleep(0.5)
print("According to my calculation you are:")
time.sleep(1)
print()
print(str(days) + " days old")
print(str(hours) + " houts old")
print(str(minutes) + " minutes old")
print(str(seconds) + " seconds old")


