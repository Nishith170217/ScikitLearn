student = ('Nishith','Nürnberg','AI') # Tuple
name,city,major = student # Tuple unpacking
print('Name= ',name)
print('City= ',city)

a = [2,3,4,5,22,1,11]
a.append(34)
print(a)
t = tuple(a) #Converting list into a tuple
#t.append(44) Tuple doesnt support append onr insertation
print(t)