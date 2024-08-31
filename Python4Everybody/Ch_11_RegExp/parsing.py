# various ways to parse str (review of previous examples)

### Method using find and str slicing 

# From stephen.marquard@uct.ac.za Sat Jan 5 O9:14:16 2008 

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 O9:14:16 2008'
atpos = data.find('@')          # find the @ for the host name
print(atpos)

# extracting the host 
sppos = data.find(' ',atpos)    # find pos of @
print(sppos)

host = data[atpos+1 : sppos]    # find the @ extract up to but not beyond the space
print(host)                     # prints the host (uct.ac.az in this example)

### Method using double split (simpler method vs above method)

words = line.split()            # splits line based on blank spaces
email = words[1]                # this returns the email address
pieces = email.split('@')       # splits email again for host
print(pieces[1])                # prints the host 


### Regex version 

#        '@([^ ]*)'

import re 
line = From stephen.marquard@uct.ac.za Sat Jan 5 O9:14:16 2008
y = findall(@([^ ]*), lin)  # '[^ ] == match non blank, '*' == many of them / greedy match
print(y)                    # prints the host


## Fine-tuned Regex version  '^From .*@([^ ]*)'
import re 
line = From stephen.marquard@uct.ac.za Sat Jan 5 O9:14:16 2008
y = findall('^From .*@([^ ]*)',lin)
print(y)                    # prints the host (search more refined)
