# define a dictonary
purse = dict()
purse['money'] = 12

# create a dictionary in another way
d1 = {'apple': 'green','banana':'yellow'}
print(d1)# prints items present in dictionary d1

# you dont have to append, just define a new key value
purse['candy'] = 3
purse['tissues'] = 75

# get the dictonary value
print(purse)
print(purse['candy'])

#replicate of current dictonary
purse1 = purse.copy() # copies all current data present in purse to purse1 dictionary
print(purse1)

#print key values of purse
print(purse.keys())

# update the dictonary value
purse['candy'] = purse['candy'] + 2
print(purse['candy'])

# Update dictionary in another way
d1.update({'mango': 'yellow'})
print(d1)#prints updated d1

