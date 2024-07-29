fname = input('Enter the name of the file: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts_mail = dict()
counts_hours = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    hours = words[5].split(':')
    if words[1] not in counts_mail:
        counts_mail[words[1]] = 1
    else:
        counts_mail[words[1]] += 1
    if hours[0] not in counts_hours:
        counts_hours[hours[0]] = 1
    else:
        counts_hours[hours[0]] += 1

lst = list()
# taking the values of the dict and transforming
for key, value in list(counts_mail.items()):
    lst.append((value, key))                    # in a list of tuple

lst.sort(reverse=True)
print(lst[0][1], lst[0][0])

list_hours = list()
for key, value in list(counts_hours.items()):
    list_hours.append((key, value))

list_hours.sort()
print(list_hours)

#time.sleep(3)
#os.system('cls')