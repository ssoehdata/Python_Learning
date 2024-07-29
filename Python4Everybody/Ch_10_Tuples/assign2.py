dict_hours = dict()
lst = list()

fname = input('Enter file name to open:')
if len(fname) < 1: fname = 'mbox-short.txt'

fhandle = open(fname)


for line in fhandle:
    wds = line.split()
    if len(wds) < 5 or wds[0] != 'From':
        continue


    colon_pos = wds[5].find(':')
    hour = wds[5][:colon_pos]
    if hour not in dict_hours:
        dict_hours[hour] = 1    # first entry
    else:
        dict_hours[hour] += 1   # additional entries counter
for key, val in list(dict_hours.items()):
    lst.append((key,val))       # fills list with hour, count of dict 
lst.sort()

for key, val in lst:
    print(key, val)

