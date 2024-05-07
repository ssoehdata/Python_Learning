# Parsing and Extracting 

# below looks for the '@' in the given string 
# and prints its position in the string (remember , starts at 0)
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

# below command starts at '@', then looks forward for space ' '
sppos = data.find(' ',atpos)
print(sppos)

# let's say we want the host for the above email:
# it starts searching from the @ sign, then
# goes one beyond the @ sign, then slices off the space position (sppos)

host = data[atpos+1 : sppos] # without the + 1 it would print the @
print(host) 