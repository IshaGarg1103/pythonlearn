#question 4
#write a program that accepts numerator and denominator of a fractional number
#and calls a user defined function mixedFraction(), when the fraction formed is not a proper fraction.
#the default value of denominator is 1. The function displays a mixed fraction only
#if the fraction formed by the parameters does not evaluate to a whole number

def mixedFraction(num,deno):
    remainder = num%deno
    if remainder!=0:
        quotient = int(num/deno)
        print("the mixed fraction = ",quotient,"(",remainder,"/",deno,")")
    else:
        print("the given fraction evaluates to a whole number")

num=int(input("Enter the numerator :"))
deno=int(input("Enter the denominator :"))
if num > deno :
    mixedFraction(num,deno)
else:
    print("It is a proper fraction")
print("end of program")