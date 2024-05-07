# Skipping (search) with continue

# can skip a line with the continue statement

fhand = open('mbox-short.txt')
for line in fhand: 
    line = line.rstrip()
    if not line.startswith('From:'):  # skips over lines we don't want (those beginning with  "From")
        continue
    print(line)
    


