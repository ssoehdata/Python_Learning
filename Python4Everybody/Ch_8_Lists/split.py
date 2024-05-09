# split() function works on strings and lists

# split() with no parameters looks for spaces,
# but will treat multiple spaces as a single space by default


abc = "with three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])


print(stuff)
for x in stuff:
    print(x)


line = 'A lot                              of spaces'
print(line)
thing = line.split()
print(thing)

# you can specify the delimiter 
line = 'first;second;third'
thing = line.split(';')
print(thing)
print(len(thing))

