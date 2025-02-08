class student:

    def __init__(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa

    def on_honor_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

#self-is a convention used as the firs parameter in instance methods of a class.
#it refers to the current instance of the class, allowing you to access
#and modify the attributes and methods of that specific instance
#self is used to distinguish between the local variable and instance variable
#without self it would treat it as a local variable within the method
