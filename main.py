import random
from wordlist import *

def create_map(word):
    map = ''
    for i in word:
        map += '_' 
    return list(map)

random_number = random.randint(0 , len(word_list))
words = word_list[random_number]
hangman_word = ''
word_to_convert = create_map(words)

while True:

    print(word_to_convert)
    player_input = input("Guess a letter\n~> ").lower()
    for i, char in enumerate(words):
        if char == player_input:
            word_to_convert[i] = char