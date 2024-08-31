# non greedy matching 

import re 
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)  # adding the trailing '+?:' 
                            # tells it to prefer the shortest str match
print(y)
