def main():
    path_name = "books/frankenstein.txt"
    text = get_book_txt(path_name)
    print(text)

def get_book_txt(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()
