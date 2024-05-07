# using a loop to filter /catch values we are looking for
# by using a conditional (if)

print('Before')
for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number', value)
print('After')
