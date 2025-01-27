#functions in Tuple

#len(tuple1)

#tuple() #tuple function takes only one function
tuple1=tuple('aeiou')
tuple1 #('a', 'e', 'i', 'o', 'u')

#count()
tuple1 = (10,20,30,10,40,10,50)
tuple1.count(90) #0

#index()
tuple1=(10,20,30,30)
tuple1.index(30) #2
tuple1.index(3)  #error : x is not in tuple

#sorted() : sorts the list in ascending order
#max, min,sum
#sum can't be operated for tuple with string data type