# string library
# python has a number of string functions incl in the str library

# these functions are already built into every string.
# we invoke them by appending the function to the string variable

greet = "Hello Dave"
zap = greet.lower()
print(zap)

print(greet)

print('Hi there'.lower())


# these functions do not modify the original string,
# instead they return a new string that has been altered
# python is using methods on the string object 
# e.g. 'greet' in above ex. is a string object lower() is a method
# below we call this method on the constant 'Hi there' 
# note constants are objects as well

# it calls the method 'lower()' on the string 'Hi there' to return
# hi there as per the methods residual return value
# print('Hi there'.lower())

# a method call is a special type of a function call 
# thing.function name  
# versus   functionname(passed something in here as a paramater)
# e.g. len(x)

# the object orientated version would be 'x.something()'


