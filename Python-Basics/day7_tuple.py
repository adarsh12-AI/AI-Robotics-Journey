tup=(1,2,3,4,5,3,3,3)
print(type(tup))
print(len(tup))
tu=(1,) # to  use it as tuple
print(tup[1:3])
print(tup.index(3))# it will give the index 
print(tup.count(3))# it wiil count 
print(tup[0])# first element
for i in tup:# print all element in tuple by loop
    print(i)
# Find sum of tuple elements.
total=0
for i in tup:
    total+=i
print(f"total sum od tuple {total}")
# Find largest element.
largest=tup[0]
for i in tup :
    if i> largest :
        largest=i
print(largest)
# Linear Search in list 
l=[10,2,3,3,4,5,3,4,3,28]
target=3
search=False
for i in l:
    i==target 
    search =True
print(search) 
# frequency count
count=0
num= int( input("enter no which you need to count the frequency "))
for i in l:
    if i==num:
        count+=1
print(count)