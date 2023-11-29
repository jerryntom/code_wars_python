import re

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
              '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
              '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
              '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_bits(bits):
    negative_bit_groups = re.findall(r'0+', bits)

    if bits[0] == '0':
        bits = bits.removeprefix(negative_bit_groups[0])

    if bits[len(bits) - 1] == '0':
        bits = bits.removesuffix(negative_bit_groups[len(negative_bit_groups) - 1])

    negative_bit_groups = re.findall(r'0+', bits)
    positive_bit_groups = re.findall(r'1+', bits)

    lengths_negative_bit_groups = [len(bit_group) for bit_group in negative_bit_groups]
    lengths_positive_bit_groups = [len(bit_group) for bit_group in positive_bit_groups]

    time_unit_1 = None
    time_unit_2 = None
    time_unit = None

    try:
        time_unit_1 = min(lengths_positive_bit_groups)
        time_unit_2 = min(lengths_negative_bit_groups)

        if time_unit_1 < time_unit_2:
            time_unit = time_unit_1
        else:
            time_unit = time_unit_2
    except ValueError:
        if time_unit_1 is None:
            time_unit = time_unit_2
        elif time_unit_2 is None:
            time_unit = time_unit_1

    for symbol in bits:
        if symbol not in '10':
            return None

    return bits.replace('111' * time_unit, '-').replace('000' * time_unit, ' ').replace('1' * time_unit, '.').replace(
        '0' * time_unit, '')


def decode_morse(morse_code):
    for symbol in morse_code:
        if symbol not in '-. ':
            return None

    morse_code_parts = morse_code.split(' ')
    final_word = ''

    for morse_code_part in morse_code_parts:
        if morse_code_part != '':
            final_word += MORSE_CODE[morse_code_part]
        else:
            final_word += ' '

    return final_word
