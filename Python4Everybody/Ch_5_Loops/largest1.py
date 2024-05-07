largest_so_far = - 1   # our var w/ initial value
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]: # 1st for loop, the_num = iteration var
    if the_num > largest_so_far:
        largest_so_far = the_num # store current largest num , assign this val to the_num var
    print('Largest so far', largest_so_far, the_num) # prints largest value so far, also prints the current value 
                                    # assigned to var the_num, then continues to loop
print('After', largest_so_far)