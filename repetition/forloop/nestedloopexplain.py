#explanation of declaration of 2-d list
#list = [[0 for i in range(column)] for j in range(row)]

# Using a list comprehension
numbers = [x for x in range(5)]

# Equivalent code using a traditional loop
numbers = []
for x in range(5):
    numbers.append(x)

#so for [0 for i in range(col)] creates a list of say col=4 then list=[0,0,0,0] 
#then say this list is called arr=[0,0,0,0] 
#the rest of the code [arr for j in range(row)] creates the nested loop of say row=3 as follows:
#[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
