# guessing by computer a secret word between 0 to 100
# the user think of a number and the computer will guess it using bisection search

low = 0
high = 100

print('Please think of a number between 0 to 100!')
print()
while True:
    guess = int((low + high) / 2)
    print('Is your number ' + str(guess) + '?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                "Enter 'c'\nto indicate I guessed correctly. ")
    if ans == 'h':
        high = guess
        guess = int((low + guess) / 2)

    elif ans == 'l':
        low = guess
        guess = int((high + guess) / 2)

    elif ans == 'c':
        print("Game over. Your secret number was: {0}".format(str(guess)))
        break
    else:
        print("Sorry, I did not understand your input")
