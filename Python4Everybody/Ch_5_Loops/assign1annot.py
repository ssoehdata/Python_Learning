
largest = None  # set variable value
smallest = None # set variable value

while True:     # begin  while loop
    value = input('Enter a number: ')   
    if value == 'done':
        break  
    try:
        intvalue = int(value) # confirm value is an int / converts to an int
    except:
        print('Invalid input') 
        continue              # keeps prog running in case of invalid input
    
    if smallest is None:
        smallest = intvalue   # sets the smallest value to input if None (our initial value)
    elif intvalue < smallest: # compares if less than current smallest value
        smallest = intvalue   # if returns true , then sets that as the current
                              # current smallest value      
       
    if largest is None:         # same as above but in reverse direction
         largest = intvalue     # to set largest values inputted
         
    elif intvalue > largest:
        largest = intvalue
            
print('Maximum is', largest)   # returns to screen max and min values
print('Minimum is', smallest)