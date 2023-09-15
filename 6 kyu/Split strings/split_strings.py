def solution(s):
    str_parts = []

    for i in range(0, len(s), 2):
        str_parts.append(s[i:i + 2])

    last_index = len(str_parts) - 1

    if str_parts != [] and len(str_parts[last_index]) == 1:
        str_parts[last_index] += '_'

    return str_parts
