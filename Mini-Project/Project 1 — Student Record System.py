#Project 1 — Student Record System
#Features:
#Add student
#Store marks
#Print student details
#Search student
#Concepts used:
#dictionary
#loops
#conditions
student={}
while True:
    print("1. Add/Update Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    print(f"Your choice is: {choice}")
   
    if choice==1:#add student
            name=input("Enter Name:")
            if name in student:
                  print("Name exist :")
                  marks=int(input("Enter new marks:"))
            else:
                marks=int(input("Enter Marks of the student:"))

            student.update({name:marks})
            
    elif choice==2:
            if len(student)==0:
                  print("No students found")
            else:
                for name,marks in student.items():
                    print(name,marks)
            
    elif choice==3:
            search=input("Enter name which you want to search:")
            if search in student:
                print(f"{search} found")
                print(f"Marks:{student[search]}")
            else :
                print("not found")
            
    elif choice==4:
            print("exit")
            break
    else:
          print("Invalid choice")
            