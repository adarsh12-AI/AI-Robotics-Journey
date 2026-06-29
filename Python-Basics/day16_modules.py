import math as m
import operation_module as op

x=int(input("Enter no to find square:"))
square=m.pow(x,2)
print(f"the square is {square}")
num=int(input("enter no to find square root:"))
root=m.sqrt(num)
print(f"the root is {root}")
num1=int(input("enter no to find factorial:"))
fac=m.factorial(num1)
print(f"the factorial is {fac}")

num2=int(input("enter first no:"))
num3=int(input("enter second no:"))
print(f"addition is {op.add(num2,num3)}")
print(f"subtraction is {op.sub(num2,num3)}")
print(f"multiplication is {op.mult(num2,num3)}")
print(f"division is {op.div(num2,num3)}")

