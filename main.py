def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    count = get_count(text)
    print(count)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_count(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_count_letters(text):
    return

if __name__ == '__main__':
    main()
