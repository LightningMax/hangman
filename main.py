import random
from word_list import *
from ASCII_arts import *

def create_map(word):
    map = ''
    for i in word:
        map += '_' 
    return list(map)

random_number = random.randint(0 , len(word_list))
words = word_list[random_number]
word_to_convert = create_map(words)
player_lives = 6
hangman_stage = 0

while player_lives > 0:
    print(HANGMANPICS[hangman_stage])
    print(' '.join(word_to_convert))
    player_input = input("Guess a letter\n~> ").lower()

    if player_input not in words:
        print("This letter is not in the word")
        player_lives -= 1
        hangman_stage +=1
    elif player_input in word_to_convert:
        print("You already typed this letter")
    else:
        for i, char in enumerate(words):
            if char == player_input:
                word_to_convert[i] = char