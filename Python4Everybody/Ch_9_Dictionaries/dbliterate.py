# two iteration variables
# loop though the key-value pair using two 
# iteration variables:
# the first var is the key, 
# the second is the corresponding  value for the key

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items():         # need to add the items() to get both key and value
                                    # note that this takes two arguments(aaa,bbb) 
                                    # so you need to pass two into it
    print(aaa,bbb)                  # output is key, value pair

