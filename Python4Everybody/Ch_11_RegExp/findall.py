# this code uses findall() to find the lines with email addresses 
# and extract one or more addresses from each of those lines.

import re 
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM' 
Ast = re.findall('\S+@\S+', s)
print(Ast)


# makes use of the ' \S ' two-character sequence that matches
#  a non-whitespace  cjaracter (\S).abs

# \S+  matches as many non-whitespace characters as possible. 
