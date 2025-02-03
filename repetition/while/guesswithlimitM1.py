#guessing game with limited no. of guesses
secret_word = "giraffe"
guess = ""
for i in range(5):
    guess = input("Enter your guess :")
    if guess!=secret_word:
        print("wrong guess!")
    else :
        print("you won!")
        break

#print(i) #in for loop the values of i becomes 4
if i == 4:
    print("oops, you are out of choices, you lost!")
