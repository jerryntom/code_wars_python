def create_phone_number(n):
    phone_num = '('

    for i in range(len(n)):
        if i < 3 or (i > 3 and i < 6) or i > 6:
            phone_num += str(n[i])
        elif i == 3:
            phone_num += ') ' + str(n[i])
        elif i == 6:
            phone_num += '-' + str(n[i])

    return phone_num
