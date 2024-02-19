def first_non_repeating_letter(s):
    checked_letters = []

    for i in range(len(s)):
        if s[i] in checked_letters:
            continue

        counter = 1

        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                counter += 1

            if counter > 1:
                checked_letters.append(s[i])
                break

        if counter == 1:
            return s[i]

    return ''
