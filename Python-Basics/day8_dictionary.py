# list problem palindrome
l=[]
n=int(input("how many no you need in list "))
for i in range(n):
    num=int(input("enter no "))
    l.append(num)
l2=l.copy()
l2.reverse()
print(l2)
if l==l2 :
    print("palindrome")
else : 
    print("not")
# tuple problem grade count A store the valu in list and sort A to D
t=("C","D","A","A","B","B","A")
count=t.count("A")
print(count)
l=["C","D","A","A","B","B","A"]
l.sort()
print(l)
# dictionary
info = {
    "key":"value",

}
print(type(info))
# Create dictionary of student.
# Print all values.
# Add city.
dict = {
    "student":["rahul","sumit","ram","jony"]
}
print(dict["student"])
dict["city"]=["almora","nanital","haldwani"]
print(dict)
# dic
dic={
    "student":"rahul",
    "subject":{
        "phy": 97,
        "chem": 90,
        "math": 91
    }    
}
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic["student"])#if key not present show error
print(dic.get("student1"))# if the key is not present it will say none
dic.update({"city":"delhi"})# create or update
print(dic)
# Loop through dictionary.
for key,value in dic.items():
    print(key,value)