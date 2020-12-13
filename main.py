def choose_language():
    try:
        print("================================================")
        print("Choose language / Wybierz język")
        language_version = int(input("English (1), Polski(2): "))
        if language_version == 1:
            from words import english_words
            print("You've chosen english language.")
        elif language_version == 2:
            from words import polish_words
            print("Wybrano język polski.")
        else:
            print("Wrong number, try again! / Niepoprawny numer, spróbuj ponownie!")
            choose_language()
    except Exception:
        print("You've typed wrong char, try again! / Podano nieprawidłowy znak, spróbuj ponownie!")
        choose_language()

choose_language()