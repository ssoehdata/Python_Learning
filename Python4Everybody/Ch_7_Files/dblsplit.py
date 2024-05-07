# the Double Split pattern

# split a line one way, then split one of these
# resulatant pieces again

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

words = line.split()
email = words[1]            # returns  stephen.marquard@uct.ac.za
# now will resplit this
pieces = email.split('@')   # returns ['stephen.marquard', 'uct.ac.za']
print(pieces[1])            # returns 'uct.ac.za' 
