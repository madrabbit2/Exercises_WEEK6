ticket_price=8.50
age=input('Enter your age for a cinema ticket: ')

if age >= 60 or age<=14:
    ticket_price=5.00
    print 'your ticket is ', ticket_price
else:
    print 'You''re ticket price is 8.5'
