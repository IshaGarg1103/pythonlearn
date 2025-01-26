#handling strings
#function to replace all the vowels in the string with '*'
def repl(st):
    newst=''
    for ch in st:
        if ch in 'aeiouAEIOU':
            newst=newst+'*'
        else:
            newst=newst+ch
    return newst
st=input('Enter a string :')
k=repl(st)
print(k)