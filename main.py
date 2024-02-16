def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    count = get_count(text)
    letter_lists = get_count_letters(text)

    print(f"-- Begin report of {path_to_file} --")
    print(f"{count} words found in the document\n")

    for item in letter_lists:
        char = item["character"]
        count = item["count"]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print(f"-- End of report --")


def get_text(path):
    with open(path) as f:
        return f.read()

def get_count(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_count_letters(text):
    dict_letters = {}
    lower_string = text.lower()
    
    # The .get() method retrieves the current count of a character from the dictionary,
    # defaulting to 0 if the character hasn't been encountered yet.
    # It then increments this count by 1 to update the character's occurrence.
    for char in lower_string:
        dict_letters[char] = dict_letters.get(char, 0) + 1

    # Convert the dictionary into a list of dictionaries
    list_of_dicts = [{"character": char, "count": count} for char, count in dict_letters.items()]

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts

def sort_on(dict):
    return dict["count"]

if __name__ == '__main__':
    main()
