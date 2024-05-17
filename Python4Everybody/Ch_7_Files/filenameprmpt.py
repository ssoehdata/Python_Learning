# prompt user for file name

fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:')  :
        count = count + 1
print('There were', count, 'subject lines in', fname)


# example output:
# enter the filen name: mbox.txt
# there were 1797 subject lines in mbox.txt

# Enter the the file name: mbox-short.txt
# There were 27 subject lines in mbox-short.txt

# add a try except to the above to handle bad filename input

fname = input('Enter the file name:  ')
try:                # added a try / except block where danger point is (filename input)
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:')  :
        count = count + 1
print('There were', count, 'subject lines in', fname)