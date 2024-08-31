import re 

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):  # basic version  
        print(line)

# the above code uses the regex re.search() 

# code below is the normal way in python using find()

#hand = open('mbox-short.txt')
#for line in hand: 
#    line = line.rstrip() 
#    if line.find('From:') >= 0:
#        print(line)

    
