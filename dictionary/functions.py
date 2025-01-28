#BUILT-IN FUNCTIONS

#length of the dictionary
dict1={}
len(dict1)

#converting list to dictionaries
list1=[(1,'a'),(2,'b')] #another form :list1=[[1,'a'],[2,'b']]
#tuple=((1,'a'),(2,'b')) #for tuple
dict2=dict(list1)
print(dict2) #{1: 'a', 2: 'b'}

#keys
dict1={1:'a',2:'b'}
dict1.keys() #dict_keys([1, 2]) #keys() take no argument

#values : returns a list of values in the dictionary
list1=list(dict1.values())
print(list1) #['a','b']

#items() : returns a list of tuples
tuple=()
tuple=list(dict1.items())
tuple[0][1]  #'a'

