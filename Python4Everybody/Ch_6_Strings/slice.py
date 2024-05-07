# slicing


s = 'Monty Python'
print(s[0:4])
# read the above as ' s sub zero through 4'
# means start at position 0, and up through, but not incl. position 4

print(s[6:7])



# can look at any continous section of a string
# using a colon separator ':'

# the second number is one beyond the end 
# of the slice " up to but not including"

# if the second number is beyond the end of  the string, 
# it stops at the end, as in this example:

print(s[6:20])

# if first position is omitted, it assumes the beginning. e.g.:

print(s[:2])

# similarly for last position
print(s[8:])

# if both positions are omitted, entire string is printed
print(s[:])