import random


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
