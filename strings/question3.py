#handling strings
#program to display string in reverse order
st=input("Enter a string :")
for i in range(-1,-len(st)-1,-1):
    print(st[i],end='')
    