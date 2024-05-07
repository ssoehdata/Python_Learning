# worked out excercise from Ch4 (ch5 on website)

#Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() 
# and use the function to do the computation. The function should return a value. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#  You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function. 


def computepay(hours,rate):
    #print("In computepay",hours, rate)  a debugging print step/check
                                       

    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else: 
        pay = hours * rate
    print("Returning", pay)
    return(pay)


stdh = input("Enter Hours: ")
stdr = input("Enter rate: ")
flth = float(stdh)
fltr = float(stdr)

xp = computepay(flth, fltr)

print("Pay:",xp)


# flow steps: 
# 1. function defined (line 2 )
# 2. reads the input  (lines 16 and 17, conversts to floating points 18, 19)
# 3. calls the computepay function (line 21) and passing in flth and fltr
#    to hours and rate in the def in line 2 
# 4. takes the values passed in and goes to line 6 and follows that if else block
# 5. prints and returns lines 12 and 13
# 6. what is returned in line 13, goes back into the expression in line 21 and
#    is assigned to xp as the calculated value.
# 7. Finally, it prints xp as pay in line 23.


# so we moved our computation inside of the function we defined (computepay)
