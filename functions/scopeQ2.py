#scope of a variable
#to access any variable outside the function
num=5
def myfunc1():
    num=0
    print("local value =",num)
    num=num+5
    print("After operation :",num)
myfunc1()
print("accessing num outside myfunc1",num)