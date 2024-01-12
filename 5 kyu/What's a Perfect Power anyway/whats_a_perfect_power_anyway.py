from math import log


def isPP(n):
    for i in range(2, int(n**.5)+1):
        log_res = round(log(n, i))

        if i ** log_res == n and i != n:
            res = [i, log_res]
            return res

