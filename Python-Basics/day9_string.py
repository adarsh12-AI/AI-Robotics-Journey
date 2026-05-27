str="my name is adarsh kumar.\ni am learning python"
print(str)
print(str.capitalize()) # it do not change the real string it make the duplicate of the string
print(str[0])
print(str.replace("adarsh","aadi"))
print(str[0:10])
print(str[:19])
print(str[10:])
for i in str:
    print(i)
# vowel count
count=0
for i in str:
    if i in "aeiou":
        count+=1
print(count)
# Reverse string
srt1="adarsh"
reverse=""
for i in srt1:
    reverse=i+reverse
print(reverse)
# Palindrome check
str1=input("enter string ")
reverse=""
for i in str1:
    reverse=i+reverse
if reverse==str1:      # to do reverse we can use str1[::-1]
    print("palindrome")
else:
    print("not")