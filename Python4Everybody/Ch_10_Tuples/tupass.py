# tuple assignment 
m = ('have', 'fun')
x, y = m 
print(x)

print(y)

m =  ('having', 'more fun')
x = m[0]
y = m[1]

print(m)

print(x)
print(y)
print(x,y)

addr = 'monty@python.org'
uname, domain = addr.split('@')

print(uname)
print('The domain is:', domain)
