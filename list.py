#functions of list
"""L=['ram','shayam','raju','baburao','alex']
print(L)

print(len(L)) #length of list
print(type(L)) #type of list
print(L.append('rukimi'))
print(L)
print(L.remove('ram'))
print(L)
print(L.sort())
print(L)
print(L.reverse())
print(L)
print(L.insert(1,'Himani'))
print(L)
del L[1]
print(L)
"""
# permanent ones
l=[1,2,3,4,5,6,7,8,9,10]
print(l)
l.append(12)
print(l)
l.insert(9,11)
print(l)
l.remove(12)
print(l)
l.pop()
print(l)
del l[0]
print(l)
l.sort()
print(l)
l.reverse()
print(l)

# temporary ones
print(sorted(l))
print(l[0:4])
print(list(reversed(l)))
print(l+[12,13,14,15])