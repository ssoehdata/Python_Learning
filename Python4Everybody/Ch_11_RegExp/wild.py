# use of wildcard operator with regex 
# search for lines that start with From and have an at sign

import re 
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:.+@', line):
        print(line)


# the .+ acts as a wildcard 
# it also "pushes outward"

# in this example 'From:.+@' will match lines that start 
# with From followed by one or more characters(.+), followed
# by an at-sign. 