#nested loop
row=int(input("Enter the no. of rows :"))
column =int(input("enter the no. of columns :"))
list = [[0 for i in range(column)] for j in range(row)]
print(list)
for i in range(row):
    for j in range(column):
        element=int(input("Enter the element's value :" ))
        list[i][j]=element
        print(list)

for i in range(row):
    for j in range(column):
        print(list[i][j],end =' ')
    print('\n')