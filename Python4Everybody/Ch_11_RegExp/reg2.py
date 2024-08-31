# using special chars in regex
# to refine search
# adding ^  character - signifies 'beginning of line' or, in the normal vers below
# startswith()

import re 

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# equivalent w/out regex 
#hand = open('mbox-short.txt')
#for line in hand:
    #line = line.rstrip()
    #if line.startswith('From:'):
        #print(line)
