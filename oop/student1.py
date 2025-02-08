class student:

    def info(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa

#info is used instead of __init__
#init automatically calls itself when the instance is created
#Python expects an __init__() method to handle the arguments passed during object creation

#in the case of info(), student1 and student2 as instances are not created
#they would just be the return values of the info() method, which in your case is None