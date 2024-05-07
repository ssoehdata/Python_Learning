# a simple loop that counts each letter in a 
# string and counts the number of times
# the letter 'a' character is encountered 



word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)



# 'in' keyword:
# 'letter" is the iteration variable here
# 'banana' is a six-character string
# the block (body) of code is executed once for each value
# in the sequence.

# the iteration var moves ("iterates") through all of the values 
# in the sequence
for letter in 'banana':
    print(letter)