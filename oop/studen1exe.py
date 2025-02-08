from student1 import student

student1=student() #empty instance is being created
student1.info("Oscar","Accounting",3.1) #manually calling the info method
student2=student()
student2.info("Phyllis","Business",3.8)
print(student1.name)
print(student2.name)

#instance is a specific object created from blueprint
#class -blueprint
#instance-an actual house built using that blueprint