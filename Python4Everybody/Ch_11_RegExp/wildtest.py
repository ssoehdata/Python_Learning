import re 
handle = open('test.txt')
for line in handle:
    line = line.rstrip()
    if re.search('^From:.+@',line):
        print(line)

