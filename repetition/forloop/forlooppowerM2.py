#method- 2

def result(base,power):
    k=1
    for i in range(power):
        k=base*k
    return k
base=int(input("enter the base :"))
power=int(input("Enter the power :"))
n=result(base,power)
print("resultant number :",n)