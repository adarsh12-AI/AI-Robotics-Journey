# Program 1 take age and tell adult or minor
age=int(input("Enter age:"))
if age<18:( print("Minor"))
else:(print("Adult"))
# Program 2 take no and check positive negative or zero
number=int(input("Enter number:"))
if number==0:(print("zero"))
elif number<0:(print("negative"))
else:(print("positive"))
# Program 3 Take two numbers and print bigger number
num1=int(input("enter first no:"))
num2=int(input("enter second no:"))
if num1<num2:(print("the bigger no is ",str(num2)))
elif num1==num2:(print("both are same"))
else:(print("the bigger no is ",str(num1)))
#program 4 Take marks and print pass and fail
marks=int(input("Enter marks "))
if marks>=40 :(print("pass"))
else: (print("fail"))
# program 5 check odd or even
num=int(input("Enter num "))
if num%2==0 :(print("Even"))
else:(print("odd"))
#problem 6 Take input from user and check 
user=input("username:")
if user=="admin":(print("access granted"))
else :(print("access denied"))
#program 7 Take three numbers and print largest
num1=int(input("Enter 1 no "))
num2=int(input("Enter 2 no "))
num3=int(input("Enter 3 no "))
if num1<num3 and num2<num3:(print("the largerst no is ",str(num3)))
elif num1<num2 and num3<num2:(print("the largerst no is ",str(num2)))
else :(print("the largerst no is ",str(num1)))