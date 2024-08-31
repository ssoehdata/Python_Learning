# reg exp match and extract 
import re 
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)


# replacing [0-9] with [AEIOU] - upper case vowels, would return an empty set
# as no upper case vowels are present in the above code