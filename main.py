import sys

from stats import chars_dict_to_sorted_list, count_characters, get_word_count

# Checks correct execution
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Returns a file's contents as a string
def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

book = get_book_text(sys.argv[1])
word_count = get_word_count(book)
counted_chars = count_characters(book)
sorted_list = chars_dict_to_sorted_list(counted_chars)

def print_report(path: str, words: int, list: list[tuple[str, int]]):
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {path}...\n")
    print("----------- Word Count ----------")
    # Loops over every tuple in the sorted list of characters, then omits spaces, punctuation, etc.
    print(f"Found {words} total words\n")
    print("----------- Character Count ----------")
    for item in list:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("\n============= END ===============")

def main():
    print_report(sys.argv[1], word_count, sorted_list)


if __name__ == "__main__":
    main()
