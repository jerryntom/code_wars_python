def unique_in_order(sequence):
    uniq_seq = []

    for elem in sequence:
        if len(uniq_seq) == 0 or uniq_seq[len(uniq_seq) - 1] != elem:
            uniq_seq.append(elem)

    return uniq_seq
