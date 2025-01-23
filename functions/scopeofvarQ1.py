#scope of a variable
#to access any variable outside the function
num=5
def myfunc1():
    global num
    print("accessing num=",num)
    num=10
    print("num reassigned =",num)
myfunc1()
print("accessing num outside myfunc1",num)