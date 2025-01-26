#functions for string
#length of a string
str='hello world'
len(str)
#title
str.title() #Hello World
str.lower()
str.upper()

#count
str='Hello World! hello Hello'
str.count('Hello',12) #1#case sensitive
str.count('Hello') #2

#find: finds the index with which word starts
str='Hello World! hello hello'
str.find('hello',10,20) #index:13
str.find('world')#-1(not found)

#index : almost same as find()
str='Hello World! hello hello'
str.index(' ') #5
str.index('Hee')#produces error: substring not found

#endswith
str='hello world '
str.endswith('d') #false
str.endswith('hello world ') #true

#startswith
str.startswith('H') #false

#isalnum()
str='hello world!'
str.isalnum() #false

#islower(), isupper()
str='!!'
str.islower() #false
str.isupper() #false

str='h!!'
str.islower() #true
str.isupper() #false

#isspace
str=''
str.isspace() #false
str='\n'
str.isspace() #true
str='\t'
str.isspace()#true
str='\r'
str.isspace() #true
str="hello\rtello"
print(str) #tello

#istitle : first letter of every word is in capital letter
str='Hello !world'
str.istitle() #false
str='Hello !&World'
str.istitle() #true
str='Hello!& 123World'
str.istitle() #true
str='Hello!& 123world'
str.istitle() #false

#join()
str1='hello world'
str2='p'
str2.join(str1) #'hpeplplpopwpoprplpd'
str1.join(str2) #'p'
str2='pp'
str1.join(str2) #'phelloworldp'