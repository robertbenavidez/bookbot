def main():
    path_name = "books/frankenstein.txt"
    text = get_book_txt(path_name)
    words = word_count(text)
    letter_count = get_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(letter_count)

    print(f"--- Begin report of {path_name} ---")
    print(f"{words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def word_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

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

main()
