# searching through a file

# can place an  'if' statement in our for loop 
# to only print lines that meet some criteria


fhand = open.('mbox-short.txt')
for line in fhand: 
    if line.startstwith('From:'):
        print(line)


# 'print' function adds a newline n\
# so the above would print out: 

# Fromtexttextext\n
# \n
#Fromtextextext\n
# \n

# etc. addding a new line (empty space) in between


# how to fix the above: 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# the above will strip the /n created by the print function

# output will be: 
#Fromtexttexttext\n
#Fromtexttexttexttext\n