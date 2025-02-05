def translate(str):
    translation=""
    for letter in str:
        if letter.lower() in "aeiou" :
            if letter.isupper() is True:
                translation = translation + "G"
            else:
                translation=translation + "g"
        else:
            translation=translation+letter
    return translation

str=input("Enter a string :")
n=translate(str)
print(n)