# method get()  checks to 
# see if a key is already in a dict
# provide a default value of zero when the key
# is not yet in the dict, and then add one


# structure

# if name in counts:
#   x = counts[name]
#else:
#  x = 0
#x = counts.get(name, 0)

# example 

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

#####

#Syntax : Dict.get(key, default=None)

#Parameters: 

    # key: The key name of the item you want to return the value from
    # Value: (Optional) Value to be returned if the key is not found. The default value is None.

# Returns: Returns the value of the item with the specified key or the default value.




d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))



d = {1: '001', 2: '010', 3: '011'}
# since 4 is not in keys, it'll print "Not found"
print(d.get(4, "Not found"))




