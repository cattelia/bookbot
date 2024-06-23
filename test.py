def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)     
    num_words = get_num_words(text)     
    chars_dict = get_chars_dict(text)  
    #print(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the documents \n")
    get_report(chars_dict)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_report(chars_dict):
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    # Got help here: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    for i in sorted_dict:
        if i.isalpha():
            print(f"The '{i}' character was found {sorted_dict[i]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
