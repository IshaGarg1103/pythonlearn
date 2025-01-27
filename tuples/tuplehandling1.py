#TUPLE HANDLING
#function to compute area and circumference of the circle
def circle(r):
    area=3.14*r*r
    circumference=2*3.14*r
    tuple=(area,circumference)
    return tuple
r=float(input("Enter the radius "))
tuple1=circle(r)
(area,circumference)=tuple1
print("Area :"+str(area))
print("Circumference :"+str(circumference))