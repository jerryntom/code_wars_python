def fib_list(n):
    fib_results = []

    for i in range(0, n):
        if i == 0 or i == 1:
            fib_results.append(1)
        else:
            fib_results.append(fib_results[i-2] + fib_results[i-1])

    return fib_results


def perimeter(n):
    fib_results = fib_list(n+1)
    fib_sum = sum(fib_results)
    return fib_sum * 4
