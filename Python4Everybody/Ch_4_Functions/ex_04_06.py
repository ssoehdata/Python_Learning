# worked out excercise from Ch4 (ch5 on website)
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
