#Ex 3_5
tshirt=15
pack_post=5

print 'Cost of t-shirt=', tshirt

print '5 pound charge for postage and packaging'

amount=input('How many would you buy?')

if amount >= 10:
    pack_post=0
    tshirt=12

totalCost= (amount*tshirt) + pack_post

print 'Total cost= ', totalCost
