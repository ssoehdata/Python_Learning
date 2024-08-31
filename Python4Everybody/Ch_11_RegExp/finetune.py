# fine tuning str extraction 

import re 

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 O9:19:16 2008'

y = re.findall('\S+@\S+',x)
print(y)
# variant - the () limits the area to be matched, without it the 'From would be incl. 
# in search results and output 
z = re.findall('From (\S+@\S+)',x)
print(z)