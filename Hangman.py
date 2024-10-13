import random
stages = ['''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
+---+
  |   |
  O   |
 /|   |
      |
      |
=========
+---+
  |   |
  O   |
  |   |
      |
      |
=========
 +---+
  |   |
  O   |
      |
      |
      |
=========
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]

import random

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "-"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "-"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("*********You lost!***********")

    if "_" not in display:
        print("***********You won************")

    print(stages[lives])



