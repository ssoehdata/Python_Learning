
# split the line into words,loop through the words 
# and use a dict to count each word independently


counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Countng...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


# definite loop in dict
# although dicts are not stored in order, we can write a for loop
# that goes through all the keys in the dict and looks up 
# the values

# chuck is a key, 1 is a value
counter = {'chuck' : 1, ' fred' : 42, 'jan' : 100 }
for key in counter: 
    print(key, counter[key])


# Retrieving lists of Keys and Values

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print('printing list\n')
print(list(jjj))
print('printing list keys\n')
print(list(jjj.keys()))              # using the keys() method to get the keys
print('printing list values\n')
print(list(jjj.values()))
print('printing list items\n')
print(list(jjj.items()))            # a tuple (this ex is a 2 tuple - 2 items)
                                    # tuple is another data structure



