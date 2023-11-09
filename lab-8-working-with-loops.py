# exercise 1
# working with while loop
# importing random and writing while loop
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)

#track if guessed number is right
#set the variable to False
isGuessRight = False

#handle game logic using while loop
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

# count up to the answer
# print("Count to 10!")

# for x in range (0, number):
#     print(x)