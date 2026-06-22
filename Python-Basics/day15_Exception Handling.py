#syntax format
# try:
    # risky code
# except:
    # code if error occurs
#problem 1: create calculator and handle invalid input and divisible by 0
def func(choice) :
    def add (num1,num2):
        return num1 + num2
    def sub (num1,num2):
        return num1-num2
    def mult (num1,num2):
        return num1*num2
    def div (num1,num2):
        try:
            return num1/num2
        except  ZeroDivisionError:
            return "invalid enter non zero denominator"
    if choice=="+":
        return add
    elif choice=="-":
        return sub
    elif choice=="*":
        return mult
    elif choice=="/":
        return div
try:
    num1 =int(input("Enter first no:"))
    num2 =int(input("Enter second no:"))
except ValueError:
    print("invalid input please enter only integers.")
else:
    operation=input("Enter operation:")
    if operation not in("+","-","*","/"):
        print("invalid input please enter operation correctly")
    else:
        fun=func(operation)
        result=fun(num1,num2)
        print(result)
# Question 2 Open a file.If file doesn't exist: return file not found 
try:
    f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student.txt","r")
    data=f.read()
except:
    print("File not found")
else:
    print("File found")
finally:
    f.close
# problem 3 take age as input if user enter text return invalid input
try:
    age=int(input("Enter age:"))
except:
    print("invalid input")
else:
    print("code successfully exicuted")
# problem 4 create student search program
def search_student():
    name = input("Enter student name: ")

    found = False

    try:
        f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student.txt","r")

        for line in f:
            data = line.strip().split(",")

            if data[0].lower() == name.lower():
                print(f"Student Found")
                print(f"Name: {data[0]}")
                print(f"Marks: {data[1]}")
                found = True
                break

        if found == False:
            print("Student Not Found")

        f.close()

    except FileNotFoundError:
        print("File Not Found")
