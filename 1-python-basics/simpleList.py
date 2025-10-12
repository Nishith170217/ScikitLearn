a = [2,3,4,5,22,1,11]
a.insert(4,66) #element insertation on position 4
print(a)
a.remove(1) #Removing element
print(a)
s= 0 #For Sum
mx= a[0] #Max
mn = a[0] #Min

for i in range(len(a)):
    if a[i]> mx:
        mx = a[i]
    if a[i]< mn:
        mn = a[i]
    s+=a[i]

print('Sum = ',s)
print('Average = ',s/len(a))
print('Max = ',mx)
print('Min = ',mn)
