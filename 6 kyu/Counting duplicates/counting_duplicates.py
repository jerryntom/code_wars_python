def duplicate_count(text):
    text = text.lower()

    char_counter = {}

    for char in text:
        char_counter[char] = char_counter.get(char, 0) + 1

    char_duplicates_amount = 0

    for k, v in char_counter.items():
        if v > 1:
            char_duplicates_amount += 1

    return char_duplicates_amount
