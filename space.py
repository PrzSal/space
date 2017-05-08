from random import randint
from time import sleep
import os
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


def create_board(width, height):
	board = []
	for row in range(0,height):
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
	return board


def print_board(board):
	for row in board:
		for char in row:
			print(char, end = '')
		print()


def insert_player(board, y_pos, x_pos):
	board[y_pos][x_pos] = '✈'
	return board


def move(y_pos,x_pos,char,board):
    if char == 'a':
        x_pos -= 1
        if board[y_pos][x_pos] == '#':
            x_pos += 1
        if board[y_pos][x_pos] == '\u001b[0;32m^\'u001b[0m':
            x_pos += 1
    elif char == 'd':
        x_pos += 1
        if board[y_pos][x_pos] == '#':
            x_pos -= 1
        if board[y_pos][x_pos] == '\u001b[0;32m^\u001b[0m':
            x_pos -= 1
    elif char == 'w':
        y_pos -= 1
        if board[y_pos][x_pos] == '#':
            y_pos += 1
        if board[y_pos][x_pos] == '\u001b[0;32m^\u001b[0m':
            y_pos += 1
    elif char == 's':
        y_pos += 1
        if board[y_pos][x_pos] == '#':
            y_pos -= 1
        if board[y_pos][x_pos] == '\u001b[0;32m^\u001b[0m':
            y_pos -= 1
    return x_pos, y_pos


def insert_block(board,y_pos_block,x_pos_block):
    board[y_pos_block][x_pos_block] = '#'
    board[y_pos_block-1][x_pos_block-1] = '#'
    return board

def insert_tree(board,y_pos_block,x_pos_block):
    board[y_pos_block+4][x_pos_block+20] = '\u001b[0;32m^\u001b[0m'
    board[y_pos_block+5][x_pos_block+20] = '\u001b[0;32m^\u001b[0m'
    return board

def main():
    x_pos = 15
    y_pos = 15
    x_pos_block = 10
    y_pos_block = 10
    char = ''
    while char != 'p':
        os.system("clear")
        intro()
        os.system("clear")
        board = create_board(60,20)
        board = insert_block(board,y_pos_block,x_pos_block)
        board = insert_tree(board,y_pos_block,x_pos_block)
        x_pos, y_pos = move(y_pos, x_pos, char, board)
        board = insert_player(board, y_pos, x_pos)
        print_board(board)
        print(x_pos,y_pos)
        char = getch()
main()
