
# example of using a guardian 

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    print('Line:',line)
    wds = line.split()
    print('Words:',wds)
    # below is a "Gaurdian" pattern 
    if len(wds) < 1 :
        continue
    if wds[0] != 'From':
        print('Ignore')
        continue
    print(wds[2])


# an alternate to the above would be in place of 9 ()
# to do the following (after print('Line:',line)): 

# if line == ' ' :
#   continue

# the above skips blank lines
# would look like this: 

#han = open('mbox-short.txt')

# for line in han:
    #line = line.rstrip()
    #print('Line:',line)
    #if line == ' ':
    #   continue
    #wds = line.split()
    #print('Words:',wds)   
    #if wds[0] != 'From':
        #print('Ignore')
        #continue
    #print(wds[2])


    