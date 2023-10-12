def find_it(seq):
    num_counter = {}

    for num in seq:
        num_counter[num] = num_counter.get(num, 0) + 1

    for k, v in num_counter.items():
        if v % 2 != 0:
            return k
