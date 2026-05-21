# program 1 print number from 1 to 10
for i in range(11):
    print(i)
#program 2 Print even numbers from 1 to 20
x=1 
while x<=20:
    if x%2==0:print(x)
    x+=1
#program 3 Print multiplication table of any number.
num=int(input("enter no "))
for i in range(11):
    print(str(num)+"*"+str(i)+"="+str(num*i))
# program 4 Find sum of numbers from 1 to any num
num=int(input("enter no "))
sum=0
for i in range(num+1):
    sum =sum + i
print(sum)
# program 5 take password repeatedly until correct password entered
password="Adarsh"
while True :
    passw=input("Enter password ")
    if password==passw:
        print("access granted")
        break
    else:
        print("wrong password")

# program 6 Count how many numbers are divisible by any no in any range
num= int(input("enter no to give a range "))
num2= int (input("by which you divisible "))
count=0
for i in range(1,num+1):
    if(i%num2==0):
        count=count+1
print(count)
#program 7 Reverse counting from any no to 1
x=int(input("enter no "))
while x>0:
    print(x)
    x=x-1