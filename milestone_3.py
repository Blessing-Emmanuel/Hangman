import random

word_fruits = ['bananas', 'apples', 'grapes', 'pears', 'pineapples']

word = random.choice(word_fruits)

def ask_for_input():
    while True:
        guess = input("Guess a letter:")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character")
    check_guess(guess)


def check_guess(guess):
    lower_guess = guess.lower()
    if lower_guess in word:
        print(f"Good guess! {guess} is in word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")


input1 = ask_for_input()
print(input1)
