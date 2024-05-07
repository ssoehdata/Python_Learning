<<<<<<< HEAD:Python4Everyboy/Ch_2_Variables/assignment2.py
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. # Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You #should #use input to read a string and float() to convert the string to a number. 
=======
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. # Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You # should #use input to read a string and float() to convert the string to a number. 
>>>>>>> b83fee8 (adding assignments dir):Python4Everyboy/Ch_2_Variables/Assignments/assignment2.py
# Do not worry about error checking or bad user data.

# calculate pay by hours worked

hrs = input('Enter hours: ')
rate = input("Enter rate: ")
xp = float(hrs) * float(rate)
print(f"Pay:", xp)
