from hangman import print_border, hangman

def choose_language():
    try:
        print_border()
        print("Choose language / Wybierz język")
        language_version = int(input("English (1), Polski(2): "))
        if language_version == 1:
            print_border()
            print("You've chosen english language.")
            hangman(1)
        elif language_version == 2:
            print_border()
            print("Wybrano język polski.")
            hangman(2) 
        else:
            print_border()
            print("Wrong number, try again! / Niepoprawny numer, spróbuj ponownie!")
            choose_language()
    except Exception:
        print_border()
        print("You've typed wrong char, try again! / Podano nieprawidłowy znak, spróbuj ponownie!")
        choose_language()

choose_language()