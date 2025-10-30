from stats import number_of_words, count_each_character, sort_character_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(path)
    word_count = number_of_words(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = count_each_character(book_text)
    sorted_character_count = sort_character_count(character_count)
    for char, count in sorted_character_count.items():
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()