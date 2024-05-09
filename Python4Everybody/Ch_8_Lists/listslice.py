# lists can be sliced in the sammer manner as strings
# additional info on pos neg indexing from
# https://www.geeksforgeeks.org/python-list-slicing/

# Syntax: 
# List[Initial : End : IndexJump]
# ' :' is the slicing operator


t = [8, 5, 41, 6, 99, 615]
print(t[::])   # display a whole list using positive indexing 
# t[3:]  # means start slicing list t from position 3 until the end

# t[:3] means slice from position 0 up to but not incl. position 3

print(t[-6::1])  # using negative indexing to print whole list
print("Original list:\n", t)

print(t[1:3]) # will start  a 2nd position, then slice up to but not incl. 3rd element

print("Sliced list 't' at positions 1:3: ", (t[1:3]))


# Reverse lists :  can be generated using a neg integer as the 
# index jump argument, leaving the initial  and end as blank. 
List = ['Geeks', 4, 'geeks!']
# Initialize list


# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[::-1])

# Display sliced list
print(List[::-3])

# Display sliced list
print(List[:1:-2])


# n.b. if some slicing expressions are made that are incomputable
# then empty lists [] are generated.
# Initialize list
List = [-999, 'G4G', 1706256, '^_^', 3.1496]

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[10::2])

# Display sliced list
print(List[1:1:1])

# Display sliced list
print(List[-1:-1:-1])

# Display sliced list
print(List[:0:])
