import random
import string

def print_border():
    print("===============================================================")

def get_valid_word(language_number):
    if language_number == 1:
        from words import english_words
        words_list = english_words
    elif language_number == 2:
        from words import polish_words
        words_list = polish_words    
    word = random.choice(words_list)
    while '-' in word or ' ' in word or len(word)<2:
        word = random.choice(words_list)
    return word.upper()

def play_again(language_number):
    if language_number == 1:
        decision = input("Do you want to play again?(Y/N): ").upper()
        if decision == "Y":
            hangman(1)
        elif decision == "N":
            print_border()
            print("Thank you for playing!")
        else:
            print_border()
            print("Invalid character. Try again!")
            play_again(1)

def hangman(language_number):
    word = get_valid_word(language_number)
    word_letters = set(word)
    used_letters = set()

    # English Version
    if language_number == 1:
        lives = 8
        alphabet = set(string.ascii_uppercase)
        while len(word_letters) > 0 and lives > 0:
            print_border()
            print(f'Lives left: {lives}')
            sorted_used_letters = sorted(list(used_letters))
            print('Used letters: ', ', '.join(sorted_used_letters))

            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('Current word: ', ' '.join(word_list))
            user_letter = input('Guess a letter: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives -= 1
                    print_border()
                    print('Letter is not in word. Try again!')

            elif user_letter in used_letters:
                print_border()
                print('You have already used that character. Try again')
        
            else:
                print_border()
                print('Invalid character. Try again.')
        
        if lives == 0:
            print_border()
            print(f"You died! It was {word}!")
        else:    
            print_border()
            print(f"You've done it! It was {word}!")
        
        print_border()
        play_again(1)

    # Polish Version
    elif language_number == 2:
        alphabet = set(['L', 'O', 'B', 'C', 'R', 'X', 'F', 'I', 'T', 'J', 'H', 'S', 'G', 'M', 'N', 'E', 'V', 'K', 'W', 'Q', 'P', 'Y', 'D', 'Z', 'A', 'U','Ą','Ć','Ę','Ł','Ń','Ó','Ś','Ź','Ż'])
        print_border()
        
        while len(word_letters)>0:
            user_letter = input('Podaj literę: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
        
            elif user_letter in used_letters:
                print_border()
                print('Ta litera już została użyta. Spróbuj ponownie.')
        
            else:
                print('Niewłaściwy znak. Spróbuj ponownie.')
   