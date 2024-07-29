#### use ability to sort a list of tuples to get a sorted vers of a dict
# start with a dict

d = {'a':10, 'c':22, 'b': 1}

t = sorted(d.items())
# print the sorted version of the dict based on key in asc order
## sort by key
print(t)

# loop through this on the key ,value pairs and print them out

# can also write it w/out () e.g. for k,v in sorted(d.items()):
for (k, v) in sorted(d.items()):
    print(k,v)
    



# to sort by values instead of key (e.g. to look for most common word)
# to do this create a list of tuples in order value, key
# then loop through them to create a list of tuples

d = {'a':10, 'c':22, 'b': 1}

tmp = list()
#print(tmp)
for k,v in d.items() :
    tmp.append( (v,k))

tmp = sorted(tmp, reverse=True)
#print(tmp)
print(v, k)


# another 
d = {'a':10, 'b':1, 'c': 22}

l = list()

for k,v in d.items() :
    l.append( (v,k))
print(l)
print(l.sort(reverse=True))