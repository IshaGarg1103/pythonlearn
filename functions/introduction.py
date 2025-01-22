#addition of two numbers
def two():
    a=int(input("Enter first number :"))
    b=int(input("Enter the second number :"))
    num=a+b
    return num
num=two()
print("sum of two numbers is "+str(num))