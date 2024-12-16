# search for lines that start with 'F', followed by 
# 2 characters, followed by 'm' 


# the '..' in the ^F..m search are placeholders for 
# any strings, e.g. Fxxm, F12m, F!@m  etc.
import re 
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

