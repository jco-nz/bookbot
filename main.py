import sys
from stats import get_num_words, get_char_stats, sort_dict

def get_book_text(p_file_path) -> None:

    try:
        with open(p_file_path) as f:
            file_contents = f.read()

            return file_contents
    except Exception as excp:
        print("Couldn't read a book")
        return None



def print_report(p_file_path, p_book_content):
    num_words = get_num_words(p_book_content)
    char_dict = get_char_stats(p_book_content)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {p_file_path}...')
    print('----------- Word Count ----------')    
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    print_dictionary(sort_dict(char_dict))


def print_dictionary(char_dict):
    for key, value in char_dict.items():
        if key.isalpha():
            print(f'{key}: {value}')


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    file_path = sys.argv[1]

    book_content = get_book_text(file_path)

    if book_content:
        print_report(file_path, book_content)

if (__name__ == '__main__'):
    main()