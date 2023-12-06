def likes(names):
    text = ''

    if len(names) == 0:
        text = 'no one likes this'
        return text
    elif len(names) == 1:
        text = names[0] + ' likes this'
        return text

    for i in range(len(names)):
        if i == 1 and len(names) >= 4:
            text += names[i] + ' and '
            break

        if i == len(names) - 1:
            text += 'and ' + names[i] + ' like this'
        elif i == len(names) - 2:
            text += names[i] + ' '
        else:
            text += names[i] + ', '

    if len(names) >= 4:
        text += str(len(names) - 2) + ' others like this'

    return text
