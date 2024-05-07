smallest = None   # a type
print('Before')
for value in [9,41,12, 3,13,74,15]:
    if smallest is None:
        smallest = value     
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)


 # 'is' is stronger then '=='                                
# implies 'is the same as'
# similar to but stronger than ==
  # is not is also a logical operator
                               