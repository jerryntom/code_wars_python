def flick_switch(lst):
    bool = True
    bool_list = []

    for item in lst:
        if item == 'flick' and bool:
            bool = False
        elif item == 'flick' and not bool:
            bool = True

        bool_list.append(bool)

    return bool_list