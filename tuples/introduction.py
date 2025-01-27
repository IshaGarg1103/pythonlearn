#tuples
#introduction to tuples
tuple1=(1,2,3,4,5)#of same type
tuple2=('economics',87,'accountancy',89.6) #of different data type
tuple3=(1,2,3,[4,5])

#wrong way to assign a single element
tuple5=(20)
type(tuple5) #integer
#right way
tuple5=(20,)
type(tuple5) #tuple

#a sequence without parentheses is treated as
#tuple by default
seq=1,2,3
type(seq) #tuple

#ACCESSING ELEMENTS IN A TUPLE
tuple1=(2,4,6,8,10,12)
tuple1[15] #error: index out of range
