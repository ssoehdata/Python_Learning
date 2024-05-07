#worked excercise ch /Loops

#create an iteration variable 'num'
num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue               
    #print(fval)
    num = num + 1       # counter pattern
    tot = tot + fval    # accumulator pattern (adding a value to it)
#print('All Done')
print(tot,num, tot/num)

