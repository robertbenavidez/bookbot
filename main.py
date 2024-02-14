def main():
    path_name = "books/frankenstein.txt"
    text = get_book_txt(path_name)
    print(text)
    words = word_count(text)
    print("word count is:", words)

def word_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_book_txt(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()
