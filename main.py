words = ['reality', 'fundamental']

player_input = input("Guess a letter\n~> ")

hangman_word = ''

for i in words[0]:
    if player_input == i:
        hangman_word += player_input
    else:
        hangman_word += "_ "

print(hangman_word)