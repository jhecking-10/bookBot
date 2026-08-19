# Separates words on whitespaces and returns a count
def get_word_count(text: str) -> int:
    return len(text.split())

# Iterates over and counts every character in a string, then adds the values to a dictionary
def count_characters(text: str) -> dict[str, int]:
    char_dict: dict[str, int] = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

# Converts dictionary, sorts in descending order of ints
# sorted(dict.items()) converts key-value pairs to a list of tuples
# sorted() passes each tuple in the list to sort_on()
def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(chars_dict.items(), reverse=True, key=sort_on)

# Returns int value from tuple
def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]
