def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    count = get_count(text)
    count_letters = get_count_letters(text)
    print(count)
    print(count_letters)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_count(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_count_letters(text):
    dict_letters = {}
    lower_string = text.lower()
    
    # dict.get() method is used to check the previously occurring character in string, 
    # if its new, it assigns 0 as initial and appends 1 to it, 
    # else appends 1 to previously holded value of that element in dictionary. 
    
    for keys in lower_string:
        dict_letters[keys] = dict_letters.get(keys, 0) + 1
    
    return dict_letters

if __name__ == '__main__':
    main()
