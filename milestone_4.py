import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word)) # needs looking st
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        lower_guess = guess.lower()
        if lower_guess in self.word:
            print(f"Good guess! {guess} is in word")
            for i in self.word:
                if i == lower_guess:
                    print(i)
                    idx = self.word.index(i)
                    self.word_guessed[idx] = lower_guess
            self.num_letters = self.num_letters-1

        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have lives {self.num_lives} left")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter:")
            if not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character")
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_fruits = ['bananas', 'apples', 'grapes', 'pears', 'pineapples']

game_1 = Hangman(word_fruits, 5)
print(game_1.ask_for_input())