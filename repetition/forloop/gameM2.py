def translate(str):
    translation=""
    for letter in str:
        if letter.lower() in "aeiou":
            translation=translation + "g"
        else:
            translation=translation+letter
    return translation

str=input("Enter a string :")
n=translate(str)
print(n)