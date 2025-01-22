#question 3
#write a program using a user defined function that accepts the
#first name and lastname as arguments, concatenate them to get full name
#and displays the output as : hello isha garg

def full_name(first,last):
    print("hello",first,last)

first=input("Enter your first name :")
last =input("Enter your last name :")
full_name(first,last)