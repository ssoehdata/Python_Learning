# reading the whole file as a series of characters


fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])


# will output text in this manner: 
# texttexttext\ntexttext\n  etc