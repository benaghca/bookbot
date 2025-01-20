def main():
    with open("books/frankenstein.txt") as f:
       file_contents = f.read()
       return file_contents
       
def count_words(file_contents):
    words = file_contents.split()
    print(f"{len(words)} words found in the document")
    return len(words)
 
def count_each_char(file_contents):
    char = {}
    lowered_contents = file_contents.lower()
    for c in lowered_contents:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
    sorted_char = dict(sorted(char.items(), key=lambda item: item[1], reverse=True))
    for c in sorted_char:
        if c.isalpha():
            print(f"The '{c}' character was found {sorted_char[c]} times")
       
if __name__ == '__main__':
    file_contents = main()
    print("--- Begin report of books/frankenstein.txt ---")
    count_words(file_contents)
    print("")
    count_each_char(file_contents)
    print("--- End report ---")
