with open("polish_words.txt",'r', encoding="utf8") as f:
    polish_words = [line.rstrip('\n') for line in f]

with open("english_words.txt",'r', encoding="utf8") as f:
    english_words = [line[:-1] for line in f]