#program workingAge.py
# a program to demonstrate the use of an if statement
# with a logical and.
# written by D.H. December 1 2004

print "This program tells you if you are of working age"
print

age = input("Type in your age:  ")
print 

if age >= 16  or age < 65:
    print "You are of working age"
else:
    print "You are not of working age"
print "Goodbye"
