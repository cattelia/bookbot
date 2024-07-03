'''
 __          __         _                                           _           
 \ \        / /        | |                                         | |          
  \ \  /\  / /    ___  | |   ___    ___    _ __ ___     ___        | |_    ___  
   \ \/  \/ /    / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \       | __|  / _ \ 
    \  /\  /    |  __/ | | | (__  | (_) | | | | | | | |  __/       | |_  | (_) |
     \/  \/      \___| |_|  \___|  \___/  |_| |_| |_|  \___|        \__|  \___/ 
                                                                               
                         __   __   __          __   __  ___ 
                        |__) /  \ /  \ |__/   |__) /  \  |  
                        |__) \__/ \__/ |  \   |__) \__/  |  
                                 
'''
import time
# For terminal output.
string = " __          __         _                                           _           \n \ \        / /        | |                                         | |          \n  \ \  /\  / /    ___  | |   ___    ___    _ __ ___     ___        | |_    ___  \n   \ \/  \/ /    / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \       | __|  / _ \ \n    \  /\  /    |  __/ | | | (__  | (_) | | | | | | | |  __/       | |_  | (_) |\n     \/  \/      \___| |_|  \___|  \___/  |_| |_| |_|  \___|        \__|  \___/ \n\n                         __   __   __          __   __  ___ \n                        |__) /  \ /  \ |__/   |__) /  \  |  \n                        |__) \__/ \__/ |  \   |__) \__/  |  \n\n\n"
print(string)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #print(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    time.sleep(2)
    print(f"--- Grabbing contents ---\n")
    time.sleep(2)
    print(f"{num_words} words found in the documents \n")
    get_report(chars_dict)
    time.sleep(1)
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
