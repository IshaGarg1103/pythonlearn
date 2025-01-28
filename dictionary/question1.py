#question-1
#program to create a dictionary which stores names of the
#employee and their salary
n=int(input("Enter the no. of employees :"))
i=0
dict1={}
list=[]
tuple=()
while i<n:
    name=input("Enter the name of the "+str(i+1)+"employee :")
    salary=int(input("Enter the salary of the "+str(i+1)+"employee :"))
    tuple=(name,salary)
    list.append(tuple)
    i+=1

dict1=dict(list)
print(dict1)