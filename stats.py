def get_num_words(p_book_text: str) -> None:
    word_list = p_book_text.split()
    # print(f'{len(word_list)} words found in the document')
    return len(word_list)


def get_char_stats(p_text: str):
    char_dict = {}

    for charac in p_text.lower():
        char_dict[charac] = char_dict.get(charac, 0) + 1
    
    return char_dict


def sort_dict(p_dict):
    sorted_items = sorted(p_dict.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)
