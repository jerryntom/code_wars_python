def cakes(recipe, available):
    cake_counter = 0

    cake_available = True

    while cake_available:
        for ingriedient, quantity in recipe.items():
            if available.get(ingriedient) is None or available[ingriedient] < quantity:
                cake_available = False
                break
            else:
                available[ingriedient] -= quantity

        if not cake_available:
            break

        cake_counter += 1

    return cake_counter
