def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    print(text)

    
def get_text(path):
    with open(path) as f:
        return f.read() 


if __name__ == '__main__':
    main()
