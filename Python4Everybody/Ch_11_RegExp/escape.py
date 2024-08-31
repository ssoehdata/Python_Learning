# escape character 

# if you want a special regex char to behave normally (most of the time)
# prefix it with '\'

import re 
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)            # prints ['$10.00']
