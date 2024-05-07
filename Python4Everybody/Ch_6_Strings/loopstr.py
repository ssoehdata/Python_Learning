#looping through strings
# here is a basic indeterminate loop
fruit =  'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
####################################
# a determinant  loop (for loop)

# the iteration variable is taken care of by the 'for loop':
# below 'letter' is the iteration variable
fruit = 'banana'
for letter in fruit:
    print(letter)

####################################
# while loop 
# this loop is equivalent to above, but is much more verbose
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
   
