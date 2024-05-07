# from page 35 py4every book (added an input function to assign values)

x,y  = [int(x) for x in input('Enter 2 values with a space between them: ').split()]
print('The respective values for  x  and y are : ', x,y)

if x == y:
    print('x and y are equal')
else:
    if x < y:
            print('x is less than y')
    else: 
        print('x is greater than y')

# this combines two tests into a single conditional
# note that both conditionals must be passed for it to print
if 0 < x:
    if x <10:
        print('x is a positive single-digit number.')  
elif x < 0:
        print('x is a negative number.')
# this is similar to the above version but uses the 'and' operator to 
if 0 < y and y < 10:
    #if y < 10:
        print('y is a positive single-digit number.')

elif y < 0:
        print('y is a negative number.')
print("Thank you Dave.")
