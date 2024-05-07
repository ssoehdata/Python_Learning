num = 0  # iteration var
tot = 0.0  # running count and total
while True: 
    sval = input('Enter a number(to quit enter "done"): ')  # remember input defaults to str
    if sval == 'done':
        break
    try: 
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('All Done')
print("To quit enter 'done'")
print(tot,num,tot/num)

