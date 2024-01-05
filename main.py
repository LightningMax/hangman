def create_map(word):
    map = ''
    for i in word:
        map += '_'
    
    return list(map)

def convert_to_list(word):
    pass
    #map_word = create_map(word)
    word_to_convert = []
    for i in word:
        if i == player_input:
            word_to_convert.append(i)
        else:
            word_to_convert.append('_ ')

    return ', '.join(word_to_convert)

def convert_to_string(word):
    pass

words = ['reality', 'fundamental']
hangman_word = ''
word_to_convert = create_map(words[0])


while True:

    print(word_to_convert)
    player_input = input("Guess a letter\n~> ")
    for i, char in enumerate(words[0]):
        if char == player_input:
            word_to_convert[i] = char

#hangman_word = convert_to_list(words[0])