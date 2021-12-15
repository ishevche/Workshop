"""
main module for attack
"""
def attack_checker(ship_list:list, attaked_pole:list, attacked_cell:tuple):
    """
    works with attack process
    """
    repeat = False
    win = True
    kill = False
    for ship in ship_list:
        for section in ship:
            if section == attacked_cell:
                attaked_pole[attacked_cell[0]][attacked_cell[1]]='*'
                repeat = True
                kill = True
                #тут я чекнула, чи попало в корабель
        if repeat:
            for section in ship:
                if attaked_pole[section[0]][section[1]] != '*':
                    kill = False
                #якщо попало, то чи вбило
        if kill:
            last_index=len(ship)-1
            for column in range(ship[0][0]-1, ship[last_index][0]+2):
                for row in range(ship[0][1]-1, ship[last_index][1]+2):
                    try:
                        assert column>=0
                        assert row>=0
                        attaked_pole[column][row]='o'
                    except Exception:
                        continue
            for section in ship:
                attaked_pole[section[0]][section[1]] = '*'
            #якщо вбило, заповняєм красиво
        if repeat:
            break
        #якшо попало, нема сенсу далі проходитись
    if not repeat:
        try:
            attaked_pole[attacked_cell[0]][attacked_cell[1]]='o'
        except IndexError:
            repeat = True
        #якщо атікована клітинка мимо поля, нехай робить ще раз
    for ship in ship_list:
        for section in ship:
            if attaked_pole[section[0]][section[1]] != '*':
                win = False
            #перевіряєм, чи ще лишились живі секції кораблів
    return attaked_pole, repeat, win
