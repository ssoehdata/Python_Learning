def area_of_circle(dog):         # python is expecting one value(radius)
                                 # and thus you can rename it (here 'dog'instead of r, or radius)
                                 
    pi = 3.14 
    result = pi * dog * dog  
    return result 


radius = 5 
area = area_of_circle(radius) # argument you call in the function 
                              # (in this ex. radius), it must have the same
                              # name as the variable name you want to pass into it.
                              # However, in the area_of_circle func
                              # python knows the value you pass into the first function (area_of_circle)
                              # is the same, and thus you can rename it (her 'dog')

                            # more precisely: Only the VALUE of the variable is passed to 
                            # the function. It is then assigned to a new variable called 'dog'.
                              
print(area)

