from random import randint
import time
import os
import inventory

def intro():
    txt_open = open('intro.txt', "r")
    txt_reader = txt_open.read()
    print(txt_reader)
    txt_open.close()


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def create_board():   # width, height
    board1_open = open('board1.txt', "r")
    file_content = board1_open.readlines()
    board1_open.close()
    list_content = []
    board = []
    for element in file_content:
        board.append(list(element.strip()))
    '''for row in range(0, height):
        board_row = []
        for column in range(0,width):
            if row == 0 or row == height-1:
                board_row.append("#")
            else:
                if column == 0 or column == width -1:
                    board_row.append("#")
                else:
                    board_row.append(" ")
        board.append(board_row)
    '''

    return board


def print_board(board, y_pos, x_pos, inventory_item):
    for row in board:
        for char in row:
            print(char, end='')
        print()
    inventory.print_table(inventory_item, 'b')

def insert_player(board, y_pos, x_pos):
    board[y_pos][x_pos] = '@'

    return board


def reader_inventory(inventory, added_items):
    inventory.import_inventory(inventory, filename='import_inventory.csv')
    print(inventory)
    #inventory.add_to_inventory(inventory, added_items)



def move(y_pos, x_pos, char, board):
    item = ['!', '^', '&']
    if char == 'a':

        x_pos -= 1
        if board[y_pos][x_pos] == '#':
            x_pos += 1

    if char == 'd':
        x_pos += 1
        if board[y_pos][x_pos] == '#':
            x_pos -= 1

    if char == 'w':
        y_pos -= 1
        if board[y_pos][x_pos] == '#':
            y_pos += 1

    if char == 's':
        y_pos += 1
        if board[y_pos][x_pos] == '#':
            y_pos -= 1
    if board[y_pos][x_pos] == '!':
        inventory.export_inventory(inventory_item, filename='test1.csv')
    if board[y_pos][x_pos] in item:
        board[y_pos][x_pos] = ' '
    for elem in board:
        for n, i in enumerate(elem):
            if i == '@':
                elem[n] = ' '
    # print(board)

    return x_pos, y_pos

'''
def insert_block(board, y_pos_block, x_pos_block):
    board[y_pos_block][x_pos_block] = '#'
    board[y_pos_block-1][x_pos_block-1] = '#'
    return board


def insert_tree(board, y_pos_block, x_pos_block):
    board[y_pos_block+4][x_pos_block+20] = '\u001b[0;32m^\u001b[0m'
    board[y_pos_block+5][x_pos_block+20] = '\u001b[0;32m^\u001b[0m'
    return board
'''





def main():
    x_pos = 15
    y_pos = 15
    x_pos_block = 10
    y_pos_block = 10
    char = ''
    intro()
    time.sleep(1)
    board = create_board()
    while char != 'p':
        os.system("clear")
        inwentory = {}
        # board = insert_block(board, y_pos_block, x_pos_block)
        # board = insert_tree(board, y_pos_block, x_pos_block)
        added_items = ['ammo']
        x_pos, y_pos = move(y_pos, x_pos, char, board)
        insert_player(board, y_pos, x_pos)
        reader_inventory(inventory, added_items)

        print_board(board, y_pos, x_pos, inwentory)
        char = getch()
main()
