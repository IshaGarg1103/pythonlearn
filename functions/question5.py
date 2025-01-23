#question 5
#WAp using user defined function calcPow()
#that accepts base and exponent as arguments and returns the value base^exponent
#where base and exponent are integers

def calcPow(base,expo):
    u=base
    for i in range(1,expo):
        base=base*u
        i=i+1
    return base

base=int(input("Enter the base :"))
expo=int(input("Enter the exponent :"))
n=calcPow(base,expo)
print("result is :",n)
print("end of program")