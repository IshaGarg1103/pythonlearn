#question 1
#program to find the sum of first n natural numbers
#1. n be passed as an argument
#2. calculate sum of first n natural numbers
#3. display the sum

def num(n):
    total=0
    for i in range(1,n+1):
        total=total + i
        i = i+1
    return total
n=int(input("Enter the value of n :"))
sum=num(n)
print("sum is "+str(sum))