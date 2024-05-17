# for assignment:

# [x] Open the file romeo.txt and read it line by line. 
# [x] For each line, split the line into a list of words using the split() method. 
# [] The program should build a list of words. 
# [x] For each word on each line check to see 
#   if the word is already in the list and 
# [x] if not append it to the list. 
# [x] When the program completes, sort and print the resulting words 


new_list = []
fname = input('Enter file name to open:  ')
fhand = open(fname)

for line in fhand:
    words = line.split()        #separate words into items in list
    for word in words: 
        if word in new_list:
            continue            # account for (ignore) duplicate words
        new_list.append(word)   # adds new words to list
print(sorted(new_list))         # sorts and prints the final list 
                                # of unique words in the text