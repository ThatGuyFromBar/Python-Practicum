def can_eat(cord1, cord2):
    move_x = abs(cord1[0] - cord2[0])
    move_y = abs(cord1[1] - cord2[1])
    return sorted([move_x, move_y]) == [1, 2]
