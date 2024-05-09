# lists have some built in functions

nums = [1,2,3,4]
print("The length, max, min and sum of nums list\n")
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

# note this first method requires all the values to be stored
# simultaneously
numlist = list()   # creates an empty list 
while True:
    inp = input('Enter a number: ')
    print('To quit enter "done"')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Average: ", average)

# using the count iterator
# this method does the calculations as it iterates (but while loops suck in python)
total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:',average)

