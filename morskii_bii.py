def attack_checker(ship_list:list, attaked_pole:list, attacked_cell:tuple):
    repeat = False
    win = True
    for ship in ship_list:
        for section in ship:
            if section == attacked_cell:
                attaked_pole[attacked_cell[0]][attacked_cell[1]]='*'
                repeat = True
                kill = True
        if repeat:
            for section in ship:
                if attaked_pole[section[0]][section[1]] != '*':
                    kill = False
        if kill:
            last_index=len(ship)-1
            for column in range(ship[0][0]-1, ship[last_index][0]+2):
                for row in range(ship[0][1]-1, ship[last_index][1]+2):
                    attaked_pole[column][row]='o'
            for section in ship:
                attaked_pole[section[0]][section[1]] = '*'
        if repeat:
            break
    if not repeat:
        try:
            attaked_pole[attacked_cell[0]][attacked_cell[1]]='o'
        except IndexError:
            repeat = True
    for ship in ship_list:
        for section in ship:
            if attaked_pole[section[0]][section[1]] != '*':
                win = False
    return attaked_pole, repeat, win
