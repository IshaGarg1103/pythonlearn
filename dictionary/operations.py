#DICTIONARY OPERATIONS

#membership
dict1={'jim':1,'pam':2}
print('karen' in dict1) #false

#traversing a dictionary
#method 1
dict1={'jim':1,'pam':2}
for key in dict1:
    print(key,":",dict1[key])

#method 2
for key, value in dict1.items():
    print(key,':',value)
#-how does this work
dict1.items() #dict_items([(1, 'jim'), (2, 'pam')])
[key,item]=dict1.items() #accessing the item and keys
list=[key,item]
list[0][0] #1