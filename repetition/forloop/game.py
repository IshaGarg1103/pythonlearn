#giraffe language
#vowels-> g
#dog-> dgg
#cat-> cgt

def translate(str1):
    list1=list(str1)
    for i in range(len(list1)):
        if list1[i] in "aeiouAEIOU":
            list1[i]='g'
    k=''.join([str(x) for x in list1])
    return k

str1=input("Enter the string :")
n=translate(str1)
print(n)