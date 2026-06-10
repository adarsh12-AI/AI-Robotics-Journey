# Feature :
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Find Topper
# 5. Calculate Average
# 6. Exit
def fun(choice):
    def add_student():
        f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student and marks.txt","a")
        data=f.write(input("Enter name and marks seperated by ,:")+"\n")
        f.close()
        print("info is saved")
    def view_student():
        f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student and marks.txt","r")
        data=f.read()
        print(data)
        f.close()
    def search_student():
        search = input("Enter name of student: ")
        found = False

        f = open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student and marks.txt", "r")

        for line in f:
            data = line.strip().split(",")

            if data[0] == search:
                print(f"{data[0]} is found and the marks are {data[1]}")
                found = True
                break

        if not found:
            print("Student not in the file")

        f.close()
    def topper():
        f = open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student and marks.txt", "r")

        topper_name = ""
        highest_marks = -1

        for line in f:
            data = line.strip().split(",")

            if int(data[1]) > highest_marks:
                highest_marks = int(data[1])
                topper_name = data[0]
        print(f"{topper_name} is topper and the marks are {highest_marks}")

        f.close()
    def average():
        f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student and marks.txt","r")
        total_marks=0
        count=0
        for line in f:
            data=line.strip().split(",")
            total_marks=total_marks+int(data[1])
            count+=1
        average=total_marks/count
        print(f"The average marks is {average}")
        f.close()
    if choice==1:
        return add_student
    if choice==2:
        return view_student
    if choice==3:
        return search_student
    if choice==4:
        return topper
    if choice==5:
        return average

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Calculate Average")
    print("any no. Exit")
    choice=int(input("Enter choice: "))
    if choice in range(1,6):    
        work=fun(choice)
        result=work()
    else:
        print("exit")
        break