# combining search and extract 
import re 
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9]+', line):
        print(line)


# makes use of the regex construct: 
# ^X-.*: [0-9]+ 

# the above translates to " we want lines that start with X-, followed 
# # by zero or more characters (.*), followed by a colon(:) and then
# # a space."
# After the space we are looking for one or more characters that are either 
# a digit (0-9) or a period [0-9.]+  

# Note that inside square brackets, the period matches  an actual period
# (i.e. it is not a wildcard between the square brackets).
