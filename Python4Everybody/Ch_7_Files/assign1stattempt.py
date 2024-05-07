# Assignment:

#Write a program that prompts for a file name, 
#then opens that file and reads through the file, 
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475

# Count these lines and extract 
# the floating point values from each of the lines 
# and compute the average of those values and produce an 
# output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

#You can download the sample data at 
#http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
# To do:
# [x] extract the float values from the lines
# [x] count the number of values found and print that with value
# [x] then convert these to float 
# [x] find the avg of the floats  and print this output

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1 
    print(count)    
    x = (line[19:])  # key was assigning this to a variable
    #print(type(x))   can delete this
    #print(line[19:])
    #convert to float
    f = float(x)
    print(f)
    #print(type(f))
    

# find avg and print
    total = total + f  # note this needs to be in the loop block!!!
#print('Total: ', total)

avg = (total + f )/ (count + 1)
median = ()  
print('Median: ', median)  

print('Total :', total + f)
print('count:', count)
print('Average spam confidence: ',avg)


