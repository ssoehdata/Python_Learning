# adding a break into a loop
# break ends the curren loop and jumps to the statement
# immediately following the loop

while True:
    line = input('>')
    if line == 'done':
        break 
    print(line)
    print("Enter done to quit")
# this will after the break point run forever
#  until 'done' is entered

# continue keyword ends the current iteration in a 'for' or 'while' loop