import os
import random
import time
from word_list import *
from ascii_arts import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

random_number = random.randint(0 , len(word_list))

word_to_guess = word_list[random_number]

player_lives = 6

hangman_stage = 0

typed_words = []

list_display = []
for _ in word_to_guess:
    list_display += '_'


while True:
    clear_screen()

    print(HANGMANPICS[hangman_stage])

    # Win Condition
    display = ''.join(list_display)
    if display == word_to_guess:
        print("You Win!")
        break
    
    # Lose Condition
    if player_lives < 1:
        print("You Lose!")
        print(f"The word was {word_to_guess}")
        break
    
    print(' '.join(display))
    player_input = input("Guess a letter\n~> ").lower()
     
    if player_input in typed_words:
        print("You already typed this letter")
        time.sleep(2)
    elif player_input not in word_to_guess:
        print("Wrong letter")
        time.sleep(2)
        player_lives -= 1
        hangman_stage +=1
    
    for position, word in enumerate(word_to_guess):
        if word == player_input:
            list_display[position] = word
    
    typed_words.append(player_input)