from itertools import permutations as perms


def permutations(s):
    string_perms = set([''.join(perm) for perm in list(perms(s))])
    return list(string_perms)
