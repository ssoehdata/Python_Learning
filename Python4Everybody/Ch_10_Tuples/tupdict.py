# dicts compared to tuples 
# the 'items'  method in dicts returns a list of tuples in key:value pairs

d = {'b':1, 'a':10, 'c':22} 
t = list(d.items())
print(t)

# this allows them to be sorted
t.sort()
print('t sorted:',t)

# mulitple assignment w dictionaries 

d = {'a':10, 'b':1, 'c':22}
for key, val in d.items():
    print(val,key)


# can combine sorted technique with the for loop through key/value pair
# to print out the contents of a dict sorted by value stored in each key/val pair

d = {'a':10, 'b':1, 'c':22}
l = list() 
for key, val in d.items(): 
    l.append((val, key))

print('Printing key:val pairs for list "l":',l)

# can also reverse sort 

l.sort(reverse=True)
print("Printing reverse sorted list 'l:", l)
