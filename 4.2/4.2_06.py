recipes = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1}}


def order(*drinks):
    global in_stock
    for drink in drinks:
        can_do = True
        for part in recipes[drink]:
            if recipes[drink][part] > in_stock[part]:
                can_do = False
                break
        if can_do:
            for part in recipes[drink]:
                in_stock[part] -= recipes[drink][part]
            return drink
    return "К сожалению, не можем предложить Вам напиток"
