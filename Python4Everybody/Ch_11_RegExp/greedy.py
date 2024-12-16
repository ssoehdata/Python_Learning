# demonstrates greedy matching 
# greedy matching returns the largest possible string 

# the repeat characters (*) and (+) push outward in both directions 
# to match the largest possible string

# so, the code below returns not only 'From' but 'From: Using the : '

import re 
x = 'From: Using the  : character'
y = re.findall('^F.+:', x)
print(y)


# ^F == first character in the match is an F 

# .+ == one or more characters 

# :  == last character in the match is a colon


#   Non-Greedy 
# the .+?  returns one or more characters but not greedy

# the example below returns 'From:'

import re 
x = 'From: Using the  : character'
y = re.findall('^F.+?:', x)
print(y)


# fine-tuning str extraction 

# \S  == at least one non-whitespace  character (one or more)

# \S+ == at least one non-whitespace character (one or more)

# example below returns:
#  ['stephen.marquard@uct.ac.za']

import re 
U = 'From stephen.marquard@uct.ac.za  Sat Jan  5 09:14:16 2008'
T = re.findall('\S+@\S+', U)
print(T)

# the following: 
# ^From (\S+@)\S+) 

# would look for str starting with From followed by a space 
# then the rest of expression

import re 
U = 'From stephen.marquard@uct.ac.za  Sat Jan  5 09:14:16 2008'
T = re.findall('^From \S+@\S+', U)
print(T)


# N.B.: adding ( ) as in the example below tells it to 
# return what is inside the ( ) , although you still match 
# the strings beginning with From 
#  i.e.  what you place inside the ( ) is what is returned


import re 
U = 'From stephen.marquard@uct.ac.za  Sat Jan  5 09:14:16 2008'
T = re.findall('^From (\S+@\S+)', U)
print(T)
