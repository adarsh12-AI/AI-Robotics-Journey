import random
secret = random.randint(1, 100)
count=0
while True:
    num=int(input("Guess Number:"))
    count+=1
    if num==secret:
        print( f"you Won the total attempt are {count} ")
        break
    elif num<secret:
        print("higher")
    else:
        print("lower")
    