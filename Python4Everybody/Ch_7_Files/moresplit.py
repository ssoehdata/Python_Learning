line = 'A lot                    of spaces'  # split treats multiple spaces as one delimiter
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)

print(len(thing))

thing = line.split(';')   # you can specify the delimiter used in the splitting
print(thing)
print(len(thing))