fh = open('mbox-short.txt')   # replace mbox-short with target filename
print(fh)           # will give info about the file

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())  # upper is a method, ly is a string var
