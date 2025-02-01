secret_word = "giraffe"
guess = ""
guess_count=0
max_guess=3
out_of_guesses = False
while guess!=secret_word and not(out_of_guesses):
    if guess_count < max_guess:
        guess=input("Enter guess :")
        guess_count+=1
    else:
        out_of_guesses = True
        break
if out_of_guesses is True :
    print("you lost, you are out of limit")
else:
    print("you won")