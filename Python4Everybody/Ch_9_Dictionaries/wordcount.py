name = input('Enter file:')  # look for file
handle = open(name)          # open the file

counts = dict()              # create an empty dictionary
for line in handle:          # iteration variable to go through each line (this is a nested loop)
    words = line.split()    # split the lines into words
    for word in words:      # create a list 'words' of the split lines and iterate through them with the iterator 'word'
        counts[word] = counts.get(word,0) + 1   # count each word and add a number to it

#  at this point in the code, the count exists and is in the var 'counts'
bigcount = None # priming the loop to count both bigcount and big word (set them both to 'None')
bigword = None
for word, count in counts.items():   # goes through the key-value pairs / a 'Maximum' loop example
    if bigcount is None or count > bigcount:  # check that the key 'bigcount' is the current largest count we have seen
        bigword = word   # counts the most commonly occurring word
        bigcount = count  # number of times most common word occurs
print('bigword is:',bigword, 'bigcount is:', bigcount)

