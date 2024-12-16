import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if  len(x) > 0:
        print(x)

# the above adds () around the part of the regular expression that represents
# the floating-point number to indicate we only want 
# findall() to return the float portion of the matchin string.abs

# compare this version:  x = re.findall('^X\S*: ([0-9.]+)', line)

# with previous example: x = re.findall('^X\S*: [0-9.]+', line)

