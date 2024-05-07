# stripping whitespace

# for removing whitepaces at beg or end of strings (tab, newline etc)

#lstrip() and rstrip() remove whitespaces from left and right respectively

# strip() reomves both  beg and ending whitespaces

greet = '      Hello Dave'
greet.lstrip()
print(greet)

greet.rstrip()
print(greet)

greet.strip()
print(greet)
