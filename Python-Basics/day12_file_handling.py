# i am using the student data which is in notes 
# problem 1 read all data
f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student.txt","r")
data=f.read()
print(data)
# append the data 
f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student.txt","a")
data=f.write("\n"+input("Enter name and marks:"))
#count no of student in file 
f=open(r"C:\Users\Adarsh\OneDrive\Desktop\AI-Robotics-Journey\Notes\student.txt","r")
count=0
for i in f:
    count+=1
print (count)
# Count each char in a file.
f.seek(0)
count=0
for i in f:
    for j in i:
        count+=1
print(count)
# Count name and marks in a file
f.seek(0)
count=0
for i in f:
    words=i.split(",")
    count+=len(words)
print("name and marks ",count)
f.seek(0)
# search for student
search=input("enter student name:")
for line in f:
    data=line.strip().split(",")
    if data[0]==search:
        print(f"{data[0]} is found and the marks is {data[1]}")