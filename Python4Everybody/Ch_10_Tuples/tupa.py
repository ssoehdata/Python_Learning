t = ('a', 'b', 'c', 'd', 'e')

print(t)
print(type(t))
t1 = ('a',)
print(t1)

t2 = tuple()
print(type(t2))
print(t2)

print(t[2])

print(t[1:3])

z = tuple('lupine')
print(z)

t1 = ('a', ) + t[1:]
t1 = ('a', ) + z[1:]

print(t1)

print(t1)