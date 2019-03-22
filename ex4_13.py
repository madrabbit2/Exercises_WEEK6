#jury.py
#A program to demonstrate the use of an
#if statement using a logical or.
# written by D.H.,December 1, 2004

print "This program will calculate if you are "
print "in the age range to qualify for Jury Service"
print

age = input("How old are you: ")

if (age < 18 and age >= 70):
    print "You do not qualify for Jury Service."
    print "You have to be at least 18 years old and under 70"
    print "years old to serve on a Jury."
else:
    print "You are qualified for Jury Service"
    print "as you are at least 18 years old and under"
    print "70 years old."
