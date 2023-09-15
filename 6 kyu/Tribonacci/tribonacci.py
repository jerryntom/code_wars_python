def tribonacci(signature, n):
    res = []

    if n == 0:
        return res
    elif n < 3:
        return signature[0:n]

    res += signature

    for i in range(3, n):
        res.append(res[i - 1] + res[i - 2] + res[i - 3])

    return res
