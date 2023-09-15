def narcissistic(value):
    str_number = str(value)
    digits_sum = 0
    power = len(str_number)

    for digit in str_number:
        digits_sum += int(digit) ** power

    if digits_sum == value:
        return True

    return False
