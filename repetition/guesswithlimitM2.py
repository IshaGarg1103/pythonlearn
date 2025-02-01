secret_word = "giraffe"
guess = ""
guess_count=0

while guess!=secret_word:
    guess=input("Enter guess :")
    guess_count+=1
    if guess_count ==4:
        break
if guess_count==4:
    print("you lost, you are out of limit")
else:
    print("you won")