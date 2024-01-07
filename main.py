import os
import random
import time
from word_list import *
from ASCII_arts import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def mapping_underscore(word):
    map = ''
    for i in word:
        map += '_' 
    return list(map)

random_number = random.randint(0 , len(word_list))
word_to_guess = word_list[random_number]
player_guess = mapping_underscore(word_to_guess)
player_lives = 6
hangman_stage = 0

while True:
    clear_screen()
    print(HANGMANPICS[hangman_stage])
    formated_player_guess = ''.join(player_guess)

    if formated_player_guess == word_to_guess:
        print("You win!")
        break
    
    if player_lives < 1:
        print("You Lose!")
        break

    print(' '.join(formated_player_guess))
    player_input = input("Guess a letter\n~> ").lower()

    if player_input in player_guess:
        print("You already typed this letter")
        time.sleep(2)
    if player_input not in word_to_guess:
        print("This letter is not in the word")
        time.sleep(2)
        player_lives -= 1
        hangman_stage +=1
    for i, char in enumerate(word_to_guess):
        if char == player_input:
            player_guess[i] = char