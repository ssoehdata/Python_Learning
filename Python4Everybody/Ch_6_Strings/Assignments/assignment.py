# [x] Write code using find() and string
# [x] slicing (see section 6.10) to extract the number 
#       at the end of the line below. 
# [x] Convert the extracted value to a floating point number 
# [x]and print it out.


text = "X-DSPAM-Confidence:    0.8475"
index = text.find('0.8475')

# slice the string for the int
#print(text[21:])

x = float(text[21:])
print(x)
#print(type(x))

