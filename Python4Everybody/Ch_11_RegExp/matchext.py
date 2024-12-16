import re 
x = '2 numbers are 19 and 42'
y = re.findall('[0-9]+',x)
z = re.findall('[AEIOU]+', x)
print(y)
print(z)

