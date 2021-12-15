def check_position(field: list, ships_lst, pos1, pos2):
    """
    >>> check_position([['-', '-', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']] , [], (1, 1), (0, 1))
    'Неправильні координати'
    """
    x0 = pos1[0]
    y0 = pos1[1]
    x1 = pos2[0]
    y1 = pos2[1]
    ship = (pos1, pos2)
    whole_ship = []
    result = 0
    if (y0 == y1) or (x0 == x1):
        result = 1
        f = lambda x: abs(x[0][0] - x[1][0]) + abs(x[0][1] - x[1][1])
        if 1 <= f(ship) <= 4:
            for i in range(min(x0, x1)-1, max(x0, x1) + 2):
                for j in range(min(y0, y1)-1, max(y0, y1) + 2):
                    try:
                        if field[i][j] != '-':
                            continue
                        else:
                            return "Неправильні координати"
                    except IndexError:
                        continue
    if x0 == x1:
        for i in range(min(y0, y1), max(y0, y1)+1):
            field[x0][i] = '-'
            whole_ship.append((x0, i))
    if y0 == y1:
        for i in range(min(x0, x1), max(x0, x1)+1):
            field[i][y0] = '-'
            whole_ship.append((i, y0))
    ships_lst.append(whole_ship)

    if result:
        return "Корабель поставлено"
    else:
        return "Неправильні координати"
