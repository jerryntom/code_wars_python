def move_zeros(lst):
    counter = lst.count(0)
    lst = list(filter(lambda x: x != 0, lst))
    lst.extend([0] * counter)
    return lst
