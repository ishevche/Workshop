"""
the most important module
"""
import re


import check_ship
import morskii_bii


def print_intro():
    """
    welcome
    """
    print("""
    Hello! Welcome to Sea Battle game.
    """)


def display(field, replace_ship='.'):
    """
    shows field for player without displayed ships
    """
    for row in field:
        for element in row:
            print(element.replace('-', replace_ship), end='')
        print()


def settle_up_ships(field, player):
    """
    sets ships on their places
    """
    print(f"""
    Час розставити кораблі гравцю №{player}.
    Кожен раз, ввід має мати вигляд: <col><row> - <col><row>
    Наприклад: d5 - a5.
    Кожна колонка має бути позначеною літерою a-j, 
    кожен рядок - цифрою від 0 до 9.
    Запис d5 - a5 означає, що на клітинки a5 b5 c5 d5 треба поставити корабель.
    """)
    cols = 'abcdefghij'
    rows = '0123456789'
    regex = re.compile(r'([a-j])(\d)\s*-\s*([a-j])(\d)')
    ships = []
    display(field)
    while len(ships) < 5:
        request = input(">>>")
        if not regex.search(request):
            print("""Ввід некоректний!! 
                  Ввід має мати вигляд: <col><row> - <col><row>
                  Наприклад: d5 - a5.
                  Кожна колонка має бути позначеною літерою a-j, 
                  кожен рядок - цифрою від 0 до 9.
                  Запис d5 - a5 означає, що на клітинки a5 b5 c5 d5 
                  треба поставити корабель.
                  """)
            continue
        col1, row1, col2, row2 = regex.findall(request)[0]
        row1 = rows.index(row1)
        col1 = cols.index(col1)
        row2 = rows.index(row2)
        col2 = cols.index(col2)
        out = check_ship.check_position(field, ships,
                                        (row1, col1), (row2, col2))
        display(field, '-')
        print(out)
    return ships


def play_game(game_data):
    """
    implements playing process
    """
    cols = 'abcdefghij'
    rows = '0123456789'
    print("Починаємо гру!")
    cur_player = 1
    regex = re.compile(r'([a-j])(\d)')
    while True:
        cur_field = game_data[cur_player - 1][0]
        cur_ships = game_data[cur_player - 1][1]
        print(f"Хід {cur_player} гравця")
        display(cur_field)
        move = input(">>>")
        if move == 'exit':
            end_game(game_data)
            return
        if not regex.search(move):
            print("Дані ввечдені некоректно!")
            continue
        col, row = regex.findall(move)[0]
        row = rows.index(row)
        col = cols.index(col)
        cur_field, repeat, won = morskii_bii\
            .attack_checker(cur_ships, cur_field, (row, col))
        if not repeat:
            cur_player = 1 if cur_player == 2 else 2
        if won:
            end_game(game_data)
            return


def end_game(game_data):
    """
    ends game?
    """
    print("Поле першого гравця:")
    display(game_data[0][0], '-')
    print("Поле другого гравця:")
    display(game_data[1][0], '-')


def main():
    """
    calls functions, nothing special
    """
    print_intro()
    first_field = [['.' for _ in range(10)] for _ in range(10)]
    second_field = [['.' for _ in range(10)] for _ in range(10)]
    first_ships = settle_up_ships(first_field, 1)
    second_ships = settle_up_ships(second_field, 2)
    play_game(((first_field, first_ships), (second_field, second_ships)))


if __name__ == "__main__":
    main()
