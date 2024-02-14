def main():
    path_name = "books/frankenstein.txt"
    text = get_book_txt(path_name)
    print(text)
    words = word_count(text)
    print("word count is:", words)
    letter_count = get_chars(text)
    print('letter count', letter_count)

def word_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_chars(book):
    chars = {}

    for word in book:
        lowered = word.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_txt(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()
