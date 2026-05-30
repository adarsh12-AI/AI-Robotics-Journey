num={1,1,2,3,4,5,3,3,2,2,4}
num1={1,2,3,2,1,1}
print(num)
num.add(6)
num.remove(4)
print(num)
num.pop()
print(num)
n=num.intersection(num1)
print(n)
n=num.union(num1)
print(n)
#Remove duplicates from list using set.
l=[1,1,2,2,3,3,4,12,1,4]
l1=set(l)# l1 is unique
print(l1)
