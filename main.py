words = ['reality', 'fundamental']
hangman_word = ''

while hangman_word != words[0]:
    player_input = input("Guess a letter\n~> ")
    
    for i in words[0]:
        if player_input == i:
            hangman_word += player_input
        else:
            hangman_word += "_ "

    print(hangman_word)