#Concepts used:
#dictionary
#functions
contact={}
def fun(choice):
    def add_contact():
        name=input("Enter name: ")
        num=int(input("Enter contact number: "))
        contact.update({name:num})
    def update_num():
        name=input("Enter Name: ")
        if name in contact:
            print(f"{name} exist")
            num=int(input("Enter new contact number: "))
            contact.update({name:num})
        else:
            print(f"{name} does not exist")
    def display_contact():
        if len(contact)==0:
            print("No contact found")
        else:
            for name,num in contact.items() :
                print(name,num)
    def search_contact():
        search=input("Enter name you want to search: ")
        if search in contact:
            print(f"{search} is found and contact number is {contact[search]}")
        else:
            print("Contact not found")
    if choice==1:
        return add_contact
    if choice==2:
        return update_num
    if choice==3:
        return display_contact
    if choice==4:
        return search_contact

while True:
    print("1. add_contact")
    print("2. update_num")
    print("3. display_contact")
    print("4. search_contact")
    print("Enter any other number then choice to exit")
    choice=int(input("Enter choice: "))
    if choice in range(1,5):    
        work=fun(choice)
        result=work()
    else:
        print("exit")
        break

