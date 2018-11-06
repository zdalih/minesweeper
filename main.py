import os, sys
from minesweeper import minesweeper

KEY_RIGHT = 'd'
KEY_LEFT = 'a'
KEY_UP = 'w'
KEY_DOWN = 's'
ENTER_KEY = 'e'
FLAG_KEY = 'f'

if __name__ == '__main__':
	game = minesweeper(size = '10x10')

	while True:	
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		print(game)
		

		#TODO - FIGURE OUT HOW TO NOT HAVE TO PRESS
		#ENTER EVERY TIME

		#MESSAGE WHEN A BOMB IS HIT
		#MESSAGE WHEN WINIING
		action = input()

		if action == ord('q'):
			break
		elif action == KEY_RIGHT:
			game.moveCursor('R')
		elif action == KEY_LEFT:
			game.moveCursor('L')
		elif action == KEY_UP:
			game.moveCursor('U')
		elif action == KEY_DOWN:
			game.moveCursor('D')
		elif action == ENTER_KEY:
			game.selectCell()
		elif action ==  FLAG_KEY:
			game.toggleFlag()


	sys.exit(0)

