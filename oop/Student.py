class Student: #class is like a blueprint for a student object
    def __init__(self, name, major, gpa,is_on_probation):    #when an object is created then it is called automatically
        #() for the initialization of the attributes of the class
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation

#LETS EXPLAIN THIS
'''self-1) refers to the current object being created or modified
2) represents the specific student you are creating'''

'''self.name=name -assigns the value of the parameter to the attribute of the object
the value is stored permanently. else local variables will be created whose value will be immediately destroyed'''
""" when we are calling student in other file and we are passing in arguments
those are getting passed on to this __init__ function. they are getting in arguments. like name="jim"  
"""