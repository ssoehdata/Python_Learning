# build a list from scratch 
stuff = list()
stuff.append('book')

print(stuff)

stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)


# can do other operations using other methods (index, insert, sort etc)
# append is a method

# in operator (returns T or F )
some = [1,9,21,10,16]
print(9 in some)   # will return True
print(99 in some)   # will return False

# lists are in order and are sortable
friends = ['joe', 'glen', 'sally']
print(friends[1])
print('original list friends:',friends)
friends.sort()
print('sorted friends:',friends)
print(friends[1])
