import random
words = ["secret", "random", "temple", "stupid", "sleep"] # Function to choose a random word from a predefined list
word = random.choice(words)

name = input("What is your name? ")
print("Hello, " + name, "Lets play hangman!")

print("Start guessing...")

guesses = '' # creates an variable with an empty value

turns = 15

while turns > 0: # creates the loop for the game to function with conditions
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=""),
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lose")