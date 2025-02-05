employees_file=open("employees.txt","r")

#to check the file is readable
print(employees_file.readable()) #but if we change the mode to write, then it would give false

#to read a particular line in the file
print(employees_file.readline())
#how it works- it prints the line where the cursor is, so if we use this function
#after the read(), the cursor is at the end of the file, so readline would give blank output

print(employees_file.readlines())
#it returns the list of the lines where the cursor is placed

#to read the file
print(employees_file.read())
#after using readlines, the cursor has reached the end of file, the output would be blank file

employees_file.close()