from random import randint
import time
import os
import datetime
import inventory


def intro():
    txt_open = open('intro.txt', "r")
    txt_reader = txt_open.read()
    print(txt_reader)
    txt_open.close()


def getch():
    '''This function detects the player's keystroke.'''

    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def load_map1():
    '''In this function load map. '''

    board1_open = open('board1.txt', "r")
    file_content = board1_open.readlines()
    board1_open.close()
    list_content = []
    board = []
    for element in file_content:
        board.append(list(element.strip()))
    return board


def load_map2():
    board2_open = open('board2.txt', "r")
    file_content = board2_open.readlines()
    board2_open.close()
    list_content = []
    board = []
    for element in file_content:
        board.append(list(element.strip()))
    return board


def load_map3():
    board2_open = open('board3.txt', "r")
    file_content = board2_open.readlines()
    board2_open.close()
    list_content = []
    board = []
    for element in file_content:
        board.append(list(element.strip()))
    return board


def load_map4():
    board2_open = open('board4.txt', "r")
    file_content = board2_open.readlines()
    board2_open.close()
    list_content = []
    board = []
    for element in file_content:
        board.append(list(element.strip()))
    return board

def skip_to_load_map2(board, y_pos, x_pos):
    ''' In this function go to another map.'''

    if board[y_pos][x_pos] == '🏁':
        board = load_map2()
        return board
    else:
        return board


def skip_to_load_map3(board, y_pos, x_pos):
    if board[y_pos][x_pos] == '🏁':
        board = load_map3()
        return board
    else:
        return board


def skip_to_load_map4(board, y_pos, x_pos):
    if board[y_pos][x_pos] == '4':
        board = load_map4()
        return board
    else:
        return board


def print_board(board, inventory_item, live):
    ''' This function print board and live and change color. '''
    print('printing\n')
    for row in board:
        for char in row:
            print(char, end='')
        print()
    inventory.print_table(inventory_item, 'count,desc')
    for elem in board:
        for n, i in enumerate(elem):
            if i == '⇧':
                elem[n] = '\033[32m⇧\033[0m'
            if i == '#':
                elem[n] = '\u001b[0;32m#\u001b[0m'
    print('LIVES: ', live)


def insert_player(board, y_pos, x_pos):
    board[y_pos][x_pos] = '@'
    return board


def insert_enemy(board, y_enem, x_enem):
    board[y_enem][x_enem] = '|'
    return board


def move(y_pos, x_pos, char, board):
    '''In this function improve move and block go hero in to wall'''

    old_x = x_pos
    old_y = y_pos

    if char == 'a':
        x_pos -= 1
    if char == 'd':
        x_pos += 1
    if char == 'w':
        y_pos -= 1
    if char == 's':
        y_pos += 1

    if board[y_pos][x_pos] not in ['i','⌷','#', '[',']', '{','}', '\u001b[0;32m#\u001b[0m', '!', '⇧', '\033[32m⇧\033[0m']:
        return x_pos, y_pos, board
    else:
        return old_x, old_y, board


def add_to_inventory(inventory, added_item):
    ''' Import inventory and add equimpent to inventory'''

    if added_item not in inventory:
            inventory.update({added_item: 0})
    for key in inventory:
        if key == added_item:
            inventory[key] += 1
    return inventory


def add_to_dict(board, x_pos, y_pos, inventory):
    ''' Add item to inventory '''

    if board[y_pos][x_pos] == '💉':
        add_to_inventory(inventory, 'painkillers')

    if board[y_pos][x_pos] == '🔫':
        print('Find secret place front door with next item')
        add_to_inventory(inventory, 'plasmagun')

    if board[y_pos][x_pos] == '👘':
        add_to_inventory(inventory, 'suit')


    if board[y_pos][x_pos] == '$':
        add_to_inventory(inventory, 'gold')


def deleting_ape_from_old_postion(board):
    '''Delete snake efect hero'''

    for elem in board:
        for n, i in enumerate(elem):
            if i == '@':
                elem[n] = ' '


def life_hero(board, y_pos, x_pos, live):
    '''Hero go to enemy or door lost live'''

    if board[y_pos][x_pos] == '|' or board[y_pos][x_pos+1] == ']' or board[y_pos-1][x_pos] == '[' or board[y_pos-1][x_pos] == '}':
        live -= 1
        return live
    else:
        return live


def open_doors(board, x_pos, y_pos, inventory):
    '''This funcions give effect open doors after accions hero'''

    if board[y_pos][x_pos] == '?':
        print('Open Doors')
        board[y_pos][x_pos] = ' '
        for elem in board:
            for n, i in enumerate(elem):
                if i == ']':
                    elem[n] = ' '

    if board[y_pos-2][x_pos] == '[':     #board[y_pos+1][x_pos+1] == '-'
        board[y_pos-2][x_pos] = ' '
    inv = sum(inventory.values())

    if inv == 2:
        for elem in board:
            for n, i in enumerate(elem):
                if i == '}':
                    elem[n] = ' '

    if inv == 4:
        for elem in board:
            for n, i in enumerate(elem):
                if i == '{':
                    elem[n] = ' '


def fight_with_enemy(board, x_pos, y_pos):
    '''Import game with another file'''
    if board[y_pos][x_pos] == 'I':
        import dojo3


def fight_with_boss(board, x_pos, y_pos):
    if board[y_pos][x_pos] == '8':
        import hot_warm2


def win_info_and_save_file(spend_time):
    '''Final repo and statistic hero'''
    print("You win! It took you %s sec" % spend_time)
    name = input("enter your name: ")
    date = str(datetime.datetime.now().strftime("%d.%m.20%y %H:%M"))
    score_list = [name, date, spend_time]
    score_text = ' | '.join(score_list) + '\n'
    score_file = open('score.txt', 'a')
    score_file.write(score_text)
    high_score_file = open('score.txt', "r")
    high_score = high_score_file.read()
    print(high_score)
    high_score_file.close()


def counting_time(start_counting_time):
    end_counting_time = time.time()
    spend_time = round((end_counting_time - start_counting_time), 0)
    return spend_time


def win_scene():
    txt_open = open('win_screen.txt', "r")
    txt_reader = txt_open.read()
    print(txt_reader)
    txt_open.close()


def end_game(board, live, y_pos, x_pos):
    if live == 0 or board[y_pos][x_pos] == '*':
        win_scene()
        return True
    else:
        return False


def authors():
    txt_open = open('authors.txt', "r")
    txt_reader = txt_open.read()
    print(txt_reader)
    txt_open.close()

def main():
    x_pos = 15
    y_pos = 15
    x_enem = randint(63, 72)
    y_enem = randint(2, 18)
    added_items = []
    live = 5
    start_counting_time = time.time()
    inventory = {'lasergun': 0, 'plasmagun': 0}
    char = ''
    intro()
    time.sleep(1)
    board = load_map1()
    insert_enemy(board, y_enem, x_enem)
    while char != 'p':
        os.system("clear")
        x_pos, y_pos, board = move(y_pos, x_pos, char, board)
        open_doors(board, x_pos, y_pos, inventory)
        add_to_dict(board, x_pos, y_pos, inventory)
        board = skip_to_load_map2(board, y_pos, x_pos)
        board = skip_to_load_map3(board, y_pos, x_pos)
        board = skip_to_load_map4(board, y_pos, x_pos)
        if end_game(board, live, y_pos, x_pos):
            break
        fight_with_enemy(board, x_pos, y_pos)
        fight_with_boss(board, x_pos, y_pos)
        live = life_hero(board, y_pos, x_pos, live)
        deleting_ape_from_old_postion(board)
        insert_player(board, y_pos, x_pos)
        print_board(board, inventory, live)
        char = getch()
    spend_time = str(counting_time(start_counting_time))
    win_info_and_save_file(spend_time)
    authors()
main()
