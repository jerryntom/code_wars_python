import re


def order(sentence):
    words = sentence.split()
    is_swapped = True

    while is_swapped:
        is_swapped = False
        for i in range(0, len(words)):
            number = int(re.findall("[0-9]", words[i])[0])

            if number-1 != i:
                words[i], words[number-1] = words[number-1], words[i]
                is_swapped = True

    sorted_sentence = " ".join(words)

    return sorted_sentence
