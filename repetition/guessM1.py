secret_word = "giraffe"
while True:
    guess=input("Enter a word :")
    if guess != secret_word:
        print("guessed the wrong word")
        continue
    else:
        break
print("guessed the right word")