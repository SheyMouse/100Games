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
from decimal import Decimal

### a year for each planet ###
mercury_year = 87.97 # days
venus_year = 224.7 #days
earth_year = 365.25 #days
mars_year = 1.88 #years
jupiter_year = 11.86 # years
saturn_year = 29.45 #years
uranus_year = 84.01 # years
neptune_year = 164.79 # years
pluto_year = 248.59 # years

print ("Hello again! Welcome to the next game in the 100 Games Project")
print ("This time we're going to calculate your age in days and years on other planets in the solar system")
time.sleep(1)

print("What is your age?")
age = int(input(">>> "))

mercury_age_years = round((age * (earth_year / 87.97)),2)
venus_age_years = round((age * (earth_year / 224.7)),2)
earth_age_years = round(age,2)
mars_age_years = round(age / 1.88 ,2)
jupiter_age_years = round(age / 11.86 ,2)
saturn_age_years = round(age / 29.46 ,2)
uranus_age_years = round(age / 84.01 ,2)
neptune_age_years = round(age / 164.79 ,2)
pluto_age_years = round(age / 248.59 ,2)

time.sleep(0.5)
print()

print(str(days) + " days old")
print(str(hours) + " hours old")
print(str(minutes) + " minutes old")
print(str(seconds) + " seconds old")

print("You are " + str(mercury_age_years) + " Mercury years old")
print("You are " + str(venus_age_years) + " Venus years old")
print("You are " + str(earth_age_years) + " Earth years old")
print("You are " + str(mars_age_years) + " Mars years old old")
print("You are " + str(jupiter_age_years) + " Jupiter years old old")
print("You are " + str(saturn_age_years) + " Saturn years old old")
print("You are " + str(uranus_age_years) + " Uranus years old old")
print("You are " + str(neptune_age_years) + " Neptune years old old")
print("You are " + str(pluto_age_years) + " Pluto years old old")


