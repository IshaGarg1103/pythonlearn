# msg="hello world"
# print(msg[0])
# print(msg[-1])
# print(msg.index("h"))
# print(max(2,4.0,4))
# print(round(3.5))
# print(round(-3.5))

#taking input from the user
# name=input("Enter your name :")
# age=input("Enter your age :")
# print("hello "+name+"! Your age is "+age)

#making a simple calculator
# num1=input("Enter first number :")
# num2=input("Enter second number :")
# result=int(num1)+int(num2)
# print(result)   #here we can't enter value of any data type other than integer as an argument

#lists
#lists are mutable sequences in Python, i.e., we can change the elements of the list
friends=["karen","jim","pam","oscar","dwight"]
print(friends[1:1])
print(friends[1:-9])
print(friends[1:5])
print(friends[1:-1])
print(friends[1:0])

#list as an argument
def increment(list2):
    for i in range(0,len(list2)):
        list2[i]+=5
    print('reference of list Inside Function',id(list2))
list1=[10,20,30,40,50]
print("Reference of list in Main",id(list1))
print("The list before the function call")
print(list1)
increment(list1)
print("The list after the function call")
print(list1)