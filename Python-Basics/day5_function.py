# program 1 create the function that print greeting in name
def greet( name ):
    print("Welcome "+ name )
name=input("enter name ")
greet(name)
#program 2 Create function to add sub mult div two numbers
def fun(operation):
    def mult(a,b):
        return (a*b)
    def add(a,b):
        return (a+b)
    def sub(a,b):
        return (a-b)
    def div(a,b):
        return (a/b)
    if operation =="add":
        return add
    if operation=="sub":
        return sub
    elif operation == "mult":
        return mult
    elif operation == "div":
        return div
    
num1=int(input("enter first no "))
num2=int(input("enter second no "))
funcn=input("enter operation to do ")

func=fun(funcn)
result=func(num1,num2)
print(f"{funcn} is {result}")
#program 3 Create function to check even or odd
def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
        
    return
num=int(input("enter no "))
result=even_odd(num)    
# program 4 Create function to find cube
def cube(num):
    return pow(num,3)
num=int(input("enter no "))
result=cube(num)
print(f"the cube is {result}")
# program 5 Create multiplication table function
def table(num):
    for i in range(1,11):
        print(i*num)
    i+=1
    return
num=int(input("enter no ")) 
result=table(num)
#program 6 Create login system using function
def login(a):
    if a=="adarsh":
        return "access granted"
    else:
        return "access denied"
password=input("enter password ")
result= login(password)
print(result)