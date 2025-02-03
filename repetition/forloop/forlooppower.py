#power question
n=2**3 #8
print(n)

def result(base,power):
    k=base
    for i in range(power-1):
        base=base*k
    return base
base=int(input("enter the base :"))
power=int(input("Enter the power :"))
n=result(base,power)
print("resultant number :",n)