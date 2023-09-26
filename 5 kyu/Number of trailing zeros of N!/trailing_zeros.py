import math


def zeros(n):
    if n == 0:
        return 0

    k_max = math.log(n, 5)
    trailing_zeros = 0

    k = 1

    while k < k_max:
        trailing_zeros += (n // (5**k))
        k += 1

    return int(trailing_zeros)
