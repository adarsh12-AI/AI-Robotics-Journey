from math import * 
#problem 1 print name
print("Adarsh kumar") 
#      0123456789....
# Problem 2 some manipulation in print
name = input("Enter name:")
print(name)
print(len(name))
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.upper().isupper())
print(name.lower().islower())
print(name[0])
print(name.index("a"))
print(name.replace(name,"aadi"))
# Problem 3 number manipulation
num =int(input("Enter number:"))
print(pow(num,3))
print(sqrt(num))
print(num+5)
print(ceil(3.7))
print(floor(2.2))
print(round(2.346))
#problem 4 add two number 
#problem 5 take two numbers and print multiplication,division,modulus
a=float(input("enter first no:"))
b=float(input("enter second no:"))
print(a+b)
print(a*b)
print(a/b)
print(a%b)
#problem 6 take input and print greeting
name=input("Enter your name ")
print("Hello " + name + " nice to meet you")
#problem 7 take age and print age after 5 year
age=int(input("Enter your age "))
print("your age after 5 year is " + str(age+5))
#problem 8 area of rectangle 
length=input("enter length:")
breath=input("enter breath:")
area=int(length) * int(breath)
print(area)
#problem 9 Celsius to Fahrenheit converter
celsius=input("Enter temp in celsius ")
fahrenheit=9/5*int(celsius)+32
print(fahrenheit)
#problem 10 Take marks of 3 subjects and print total
sub_1=int(input("Enter subject 1 marks "))
sub_2=int(input("Enter subject 2 marks "))
sub_3=int(input("Enter subject 3 marks "))
print("the total marks " + str(sub_1 + sub_2 + sub_3))
#problem 11 square and cube of number
num=  int(input("Enter no "))
print("square of a number " +str(pow(num,2)))
print("cube of a number " +str(pow(num,3)))
