ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen']  + 1

print(ccc)


# in operator / can use to look for an item  in a dict

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names: 
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)
