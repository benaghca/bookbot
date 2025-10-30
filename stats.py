def number_of_words(text):
    words = text.split()
    return len(words)

def count_each_character(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_count(char_count):
    return dict(sorted(((char, count) for char, count in char_count.items() if char.isalpha()), key=lambda item: item[1], reverse=True))