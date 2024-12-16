# [x] extract the numbers in the file 
# [] cast as ints if necessary 
# [] compute the sum of the numbers 

import re 
handle = open('sampledata.txt')
for line in handle:
    line = line.rstrip() 
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
       
        print(x)

    
