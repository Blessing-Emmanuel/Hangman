import random

word_fruits = ['bananas', 'apples', 'grapes', 'pears', 'pineapples']

word = random.choice(word_fruits)

print(word_fruits)

print(word)

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That's not a valid input.")