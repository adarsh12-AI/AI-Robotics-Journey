#Problem 1 Find sum of list
l1=[2,3,4,5,6]
sum=0
for i in l1:
    sum=sum+i
print(sum)
#problem 2 Find largest element,Count even numbers,Find average,Print all list elements using loop.
l=[]
num=int(input("enter no "))
for i in range (num):
    num1=int (input("enter no which will add in list "))
    l.append(num1)
large=max(l)
print(f"the largest no is {large}")
small=min(l)
print(f"the smallest no is {small}")
count=0
for i in l:
    if i%2==0:
        count+=1
print(f"even no count is {count}")
total=0
for i in l:
    total+=i
length=len(l)
avg=total/length
print(f"the avg is {avg}")
for i in l:
    print(i)
l.sort(reverse=True)
print(l)