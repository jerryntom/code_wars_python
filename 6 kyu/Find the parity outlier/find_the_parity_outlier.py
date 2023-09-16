def find_outlier(integers):
    index_first_odd = None
    index_first_even = None
    odd_counter = 0
    even_counter = 0

    for i in range(0, len(integers)):
        if integers[i] % 2 == 0 and index_first_even is None:
            index_first_even = i
        elif integers[i] % 2 != 0 and index_first_odd is None:
            index_first_odd = i
        elif index_first_even is not None and index_first_odd is not None:
            break

    for num in integers:
        if num % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

        if odd_counter > 1:
            return integers[index_first_even]
        elif even_counter > 1:
            return integers[index_first_odd]
