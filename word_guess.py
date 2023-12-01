import random

words = ["Endler", "neon tetra", "Guppy", "Betta", "Shrimp",
         "Oscar", "Ram", "Rummy Nose", "Cory", "Discus", "Flower horn"]


random_word = random.choice(words)

print("Our random word", random_word)

print("********* WORD GUESSING GAME ***********")

user_guesses = ""
chances = 10

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"Correct guess: {character}")
        else:
            wrong_guesses += 1
            print("_")

    if wrong_guesses == 0:
        print("Correct.")
        print(f"Word: {random_word}")
        break
    guess = input("Guess a freshwater fish: ")
    user_guesses += guess

    if guess not in random_word:
        chances -= 1
        print(f"Wrong. You have {chances} changes remaining")

        if chances == 0:
            print("game over")
