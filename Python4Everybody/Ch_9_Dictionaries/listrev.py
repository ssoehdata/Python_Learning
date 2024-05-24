cards = list()
cards.append(12)
cards.append(3)
cards.append(75)

print(cards)

print(cards[1])

cards[1] =  cards[1] + 2

print(cards)


# Dictionaries use key / value pair
# like lists but uses keys instead of position(as in lists) to look up values
cabinet = dict()
cabinet['summer'] = 12          #summer is the key , 12 the value
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet)

print(cabinet['fall'])

cabinet['fall'] = cabinet['fall'] + 2

print(cabinet)


#constants in dicts
# use {}
# syntax  key :  value

jjj = {'chuck' : 1, 'fred' : 42, 'jan ': 100}
print(jjj)

ooo = { }    # empty dictionary
print(ooo)
