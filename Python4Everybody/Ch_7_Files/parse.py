# program to parse through an email


han = open('test')           # opens filename.txt

for line in han:
    line = line.rstrip()    #strips white space
    #print('Line:',line)     #debugging 
    #if line == ' ':
        #print('Skip Blank')
        #continue
    wds = line.split()       #splits the words
    #print('Words:',wds)     # debugging

    # below is a 'Gaurdian Pattern' 
    if len(wds) < 1 :
        continue        
    if wds[0] != 'From':    #checks if first word is 'From'
        #print("Ignore")      # debugging
        continue            #if above is false, continue restart loop
    print(wds[2])           # print the third word if line begins with 'From




    # the above will crash due to 'if wds[0] != 'From': if there
    # are no words (blank spaces) in a line. 

    # fix: add the following if & continue statement before that line:
    # if len(wds) < 1:
    #    continue


    ### instead of the above gaurdian pattern could use this:
    # if line == ' ' :
    #   continue       # this would be after line = line.rstrip()


    # A 'stronger ' Gaurdian: this accounts for cases 
    # if 'From' is first word, but there is only 1 word
    # that would cause a traceback on the final line

    # Fix:  simply change the if len(wds) < 3 : 
    # so we want at least 3 words in a line


    ##### Gaurdian in a compound statement #####
    # Another Guardian variant:
    # if len(wds) < 3 or  wds[0] != 'From':
    #      continue

    ### Nota bene: the above checks these in order!

    ## this is called 'Short Circuit Evaluation' #####

    # it first checks if the 'if len(wds) < 3 'statement
    # (the first of the two checks)
    # is T or F before checking  the second, if it Fails
    # this first test, it will go to next line 
    # and continue (skipping the second test)
    
    # Note bene.:
    # rearranging the order of these tests could cause the
    # program to fail

    # becuase the  'guardian ' is the if len(wds) < 3: 
    # statement