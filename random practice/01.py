#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old. 
#Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
#If you want to do this in a generic way, see exercise 39.

#Extras:

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)


name = input('Enter your name ')
age = input('Enter your age ')

fage = float(age)

fhundred = 100 - fage 

year = 2022 + fhundred

print(name," you have ",int(fhundred),"years until you turn 100 in the year",int(year))

