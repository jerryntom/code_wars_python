def hex_string_to_RGB(hex_string):
    r = hex_string[1:3]
    g = hex_string[3:5]
    b = hex_string[5:7]

    return {'r': int(r, base=16), 'g': int(g, base=16), 'b': int(b, base=16)}
