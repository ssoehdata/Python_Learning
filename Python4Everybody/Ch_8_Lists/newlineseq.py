# file handle as a sequence

# a file handle open for read can be treated as a sequence
# of strings where each line in he file is a
# string in the sequence.

# we can use a for statement to iterate through a sequence

# remember a sequence is an ordered set

xfile = open('mbox.txt')
for cheese in xfile:     # cheese is an iteration var for the for loop here
    print(cheese)           # ' for each line (cheese) in the the filehandle 'xfile'
                            # 'run this loop 1x, then print it' 