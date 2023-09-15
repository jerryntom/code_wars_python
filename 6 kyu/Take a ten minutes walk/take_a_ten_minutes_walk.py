def is_valid_walk(walk):
    x_pos = 0
    y_pos = 0
    time = 0

    for step in walk:
        if step == 'n':
            y_pos += 1
        elif step == 's':
            y_pos -= 1
        elif step == 'w':
            x_pos -= 1
        elif step == 'e':
            x_pos += 1

        time += 1

    if x_pos == 0 and y_pos == 0 and time == 10:
        return True
    else:
        return False
