set1={'MON','TUES','WED'}
print(set1)
set1.add('THURS')
print(set1)

#list as set
l=[3,6,7,8,2,34,2,2,2,2,4]
newset=set(l)
print(newset)

#dictionary as set
d1 = {'key1':'value1','key2':'value2','key3':'value3'}
newset1=set(d1)
newset2=set(d1.values())
print(newset1)
print(newset2)

#tuples as set
t1=(3,4,5,2,3,4,5,2,3,4,21)
newset3=set(t1)
print(newset3)