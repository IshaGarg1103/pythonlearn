employee_file=open("employees.txt","r")
print(employee_file.readlines()[0])
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
#WHAT EXACTLY HAPPENED IN THIS PROGRAM
#what readlines does is it read the entire file until the cursor reached the end of file, and it shows the output 
#as 'Jim-salesperson'. Now the cursor has reached the endoffile even tho it the output it shows the data of only one employee
#so when the loop runs, it shows blank output