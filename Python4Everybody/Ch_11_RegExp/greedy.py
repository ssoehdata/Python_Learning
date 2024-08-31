# greedy matching / when a string can match more than
# one possible string it matches the largest found 

import re 
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# in the above, ' From Using the : ' is returned instead of merely 'From: ' as it
# is longer 