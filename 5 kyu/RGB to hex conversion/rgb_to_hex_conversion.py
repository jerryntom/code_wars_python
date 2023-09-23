def byte_num_to_hex(num):
    if 0 <= num <= 255:
        num_hex = f'{num:02x}'.upper()
    elif num < 0:
        num_hex = '00'
    else:
        num_hex = 'FF'

    return num_hex


def rgb(r, g, b):
    return byte_num_to_hex(r) + byte_num_to_hex(g) + byte_num_to_hex(b)
