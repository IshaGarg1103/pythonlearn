#program to input n numbers from the user. store these numbers
#in a tuple. print the maximum and minimum number from this tuple
numbers =tuple()
n=int(input("how many numbers you want to enter? :"))
for i in range(0,n):
    num=int(input("Enter the "+str(i+1)+" number :"))
    tuple1=(num,)
    numbers=numbers+tuple1

print("the numbers in the tuple are :")
print(numbers)
print("The maximum number :",max(numbers))
print("The minimum number is :",min(numbers))