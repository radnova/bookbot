def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    for t in text:
        lowered = t.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def return_val(dict):
    return dict["count"]

def chars_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "count": dict[char]})
    sorted_list.sort(key=return_val, reverse=True)
    return sorted_list

def print_report(path):
    book_text = read_book(path)
    wc = count_words(book_text)
    cc = count_chars(book_text)
    sl = chars_to_sorted_list(cc)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {wc} total words")
    print(f"--------- Character Count -------")
    for i in sl:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['count']} times")
    print(f"============= END ===============")