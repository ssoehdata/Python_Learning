#prompt user for integers until 'done'
# is entered. Then print out largest
# and smallest of the numbers.
# if a non-valid number is entered
# print 'Invalid input' and ignore it
#(continue the program)

#use the following values as input:
# 7, 2, bob, 10, 4 output should read:

#Invalid output
#Maximum is 10
#minimum is 2
##################################################
# Code below is given: 

#largest = None
#smallest = None
#while True:
    #num = input("Enter a number: ")
    #if num == "done":
        #break
    #print(num)
#print("Maximum", largest)
##################################################





#print("var value  = : ",var) 
largest = num
smallest = None
var = 0
while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
        continue
    try:        
        num = int(num)
    except:
        print('Invalid input')
        continue
        print('good so far')
    if num > var:
        maximum = largest
        #print('Maximum so far is: ',largest)
    if num < var:
        smallest = smallest
        print('Minimum so far is: ', smallest)
    
print('Initial largest & smallest values: ', largest,smallest)
print(num)

print('Maximum is ', largest)
print('Mininum is ', smallest)
