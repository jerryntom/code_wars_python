def productFib(prod):
    fib_list = [0, 1]
    fib_list_pos = 2

    while True:
        two_last_fib_multi = fib_list[fib_list_pos - 2] * fib_list[fib_list_pos - 1]

        if two_last_fib_multi == prod:
            return [fib_list[fib_list_pos - 2], fib_list[fib_list_pos - 1], True]
        elif two_last_fib_multi > prod:
            return [fib_list[fib_list_pos - 2], fib_list[fib_list_pos - 1], False]

        fib_list.append(fib_list[fib_list_pos - 2] + fib_list[fib_list_pos - 1])
        fib_list_pos += 1
