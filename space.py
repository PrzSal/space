from random import randint
from time import sleep
import os

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


def create_board(width,height):
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
'''
def create_board_block(x_pos_block,y_pos_block):
	board_block = []
	for row in range(0,y_pos_block):
		board_row_block = []
		for column in range(0,x_pos_block):
			if row == 0 or row == y_pos_block-1:
				board_row_block.append("X")
			else:
				if column == 0 or column == x_pos_block -1:
					board_row_block.append("X")
				else:
					board_row_block.append(" ")
		board_block.append(board_row_block)
	return board_block
'''
def print_board(board):
	for row in board:
		for char in row:
			print(char, end='')
		print()


def insert_player(board, x_pos, y_pos):
	board[y_pos][x_pos] = '@'
	return board


def move(x_pos,y_pos,char):
    if char == 'a' and x_pos > 1:
        #if x_pos_block == x_pos:
        #    x_pos += 1
        #else: 
        x_pos -= 1
    elif char == 'd' and x_pos < 58:
        x_pos += 1
    elif char == 'w' and y_pos > 1:
        y_pos -= 1
    elif char == 's' and y_pos < 18:
        y_pos += 1
    return x_pos, y_pos        

def insert_block(board,y_pos_block,x_pos_block):
    board[x_pos_block][y_pos_block] = '#'
    board[x_pos_block-1][y_pos_block-1] = '#'
    return board #, x_pos_block, y_pos_block

def main():
    x_pos = 15
    y_pos = 15
    x_pos_block = 10
    y_pos_block = 10
    char = ''
    while char != 'p':
        x_pos, y_pos = move(x_pos, y_pos, char)
        os.system("clear")
        #board_block = create_board_block(x_pos_block,y_pos_block)
        board = create_board(60,20)
        board = insert_player(board, x_pos, y_pos)
        board = insert_block(board,x_pos_block,y_pos_block)
        print_board(board)
        char = getch()

main()