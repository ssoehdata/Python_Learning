# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)


count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    x = (line[19:])  # key was assigning this to a variable
    #print(type(x))   can delete this
    #print(line[19:])
    #convert to float
    f = float(x)
    print(f)
    print(type(f))

    





# find avg and print


#avg = (total / count)
#print(avg)
#print(line)
print("Done")
