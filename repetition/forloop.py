#introduction forloop
#for strings
for letter in "giraffe":
    print(letter,end='')
print('\n')

#forloop for list
#method 1
friends=['jim','karen','pam']
for friend in friends:
    print(friend)
#method 2
for i in range(len(friends)):
    print(friends[i])

#RANGE FUNCTION
for i in range(4,0,-1):
    print(i)
#output - 4 3 2 1

for i in range(9,8):
    print(i)
#no output
for i in range(-2,4,-1):
    print(i)