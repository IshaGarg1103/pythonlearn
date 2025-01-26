#handling strings
#function to count the number of times a character occurs
#in a string

def charCount(st,ch):
    num=st.count(ch)
    return num
st=input("Enter a string :")
ch=input("Enter the character to be searched :")
count=charCount(st,ch)
print(count)