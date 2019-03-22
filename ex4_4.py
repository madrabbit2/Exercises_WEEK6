# odd_or_even.py
# A program to determine if a whole number input from the keyboard
# is odd or even.
# written by D.H.,December 1, 2004

number = input( "Type in a whole number: ")
print
remainder = number % 3
if remainder == 0:
    print "Your number is exactly divisable by 3"
else:
    print "Your number is not divisible by 3"
