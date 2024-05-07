# example of a short-circuit guard


x = 2
y = 0
print(x,y)
x >= 2 and y != 0  and (x/y) > 2 #  here 'y != 0' is a guard that ensures it only 
                                 #executes x/y if y is a non-zero value