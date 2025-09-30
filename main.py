import sys
from stats import get_num_words 
from stats import get_num_chars
from stats import get_sorted_char_counts


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    d_list: dict = get_sorted_char_counts(get_num_chars(text))
    for kvp in d_list:
        print(f"{kvp["char"]}: {kvp["num"]}")
    print("============= END ===============")


main()
    
