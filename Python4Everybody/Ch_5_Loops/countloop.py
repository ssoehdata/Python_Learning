# from 4th lecture in ch 5(ch6 on website) on loops & iteration
# patters in loops
# counting in a loop

zork = 0                         #set variable (usually called 'count')
print('Before', zork)            # prints Beginning value of variable
for thing in [9,41,9000,3,74,15,99]:  #values in set to iterate through, thing is our iteration var
    zork = zork + 1             # add 1 to intitial var                                
    print(zork, thing)          # prints orig val + 1, and each value in set 
print('After', zork)            # prints after, and the value of the var at this final iteration
                                # this will be 7 since init var = 0, we added 1 for
                                # each iteration of the loop to the initial var
                                # i.e. how many times line 8 ran
                                # and there are 7 elements in the set


