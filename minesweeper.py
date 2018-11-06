import random

class minesweeper(object):

	'''
	We have two 2D arrays, one that keeps track of the
	private board, or where the bombs actually are.

	and the other is what the player can see
	'''

	def __init__(self, size):
		self.height, self.width = map(int,size.split('x'))
		self.privateBoard = [[0 for x in range(self.height)] for y in range(self.width)] 
		self.publicBoard = [[None for x in range(self.height)] for y in range(self.width)] 
		self.numBombs = int(self.height*self.width*0.1)
		self.cursor = (self.width//2, self.height//2)

		self.placeBombs()


	def __str__(self):

		rows = []

		row = ['\033[93m| ']
		for i in range(self.width):
			row.append(' '  + chr(97 + i) + ' ')

		rows.append('|'.join(row))

		for j in range(self.height):
			row = ['\033[93m']
			row.append(str(j))
			for i in range(self.width):
				if self.publicBoard[i][j] is None:
					cell = '\033[91m '
				elif self.publicBoard[i][j] >= 0 :
					cell = '\033[97m' + str(self.publicBoard[i][j])
				elif self.publicBoard[i][j] == -1:
					cell = '\033[91mB'

				if i == self.cursor[0] and j == self.cursor[1]:
					row.append('\033[4m ' + cell + ' \033[0m')
				else:
					row.append(' ' + cell + ' ')
				

			rows.append('\033[93m|'.join(row))

		rowDivider = ''.join(['\n\033[93m', ''.join(['-']*(len(rows[0])-5)), '\n'])
		return rowDivider.join(rows)

	def printFullBoard(self):

		rows = []

		row = ['\033[92m| ']
		for i in range(self.width):
			row.append(' '  + chr(97 + i) + ' ')

		rows.append('|'.join(row))

		for j in range(self.height):
			row = ['\033[92m']
			row.append(str(j))
			for i in range(self.width):
				if self.privateBoard[i][j] is None:
					cell = '\033[91m '
				elif self.privateBoard[i][j] == -2:
					cell = '\033[93mF'
				elif self.privateBoard[i][j] >= 0 :
					cell = '\033[94m' + str(self.privateBoard[i][j])
				elif self.privateBoard[i][j] == -1:
					cell = '\033[91mB'
				row.append(' ' + cell + ' ')

			rows.append('\033[92m|'.join(row))

		rowDivider = ''.join(['\n\033[92m', ''.join(['-']*(len(rows[0])-5)), '\n'])
		return rowDivider.join(rows)


	def placeBombs(self):
		bombIndices = random.sample(range(1,self.height*self.width), self.numBombs)
		
		for index in bombIndices:

			i = (index - 1) % self.height
			j = (index - 1) // self.height
	
			self.privateBoard[j][i] = -1

	def selectCell(self, cellTuple = None):
		if cellTuple is None:
			i = self.cursor[0]
			j = self.cursor[1]
		else:
			i = cellTuple[0]
			j = cellTuple[1]


		if self.privateBoard[i][j] == -1:
			#you've hit a bomb
			self.publicBoard[i][j] = -1
			return

		#depth first, recursive algorithm
		#that will go through cells until
		#we have hit cells that are surrounded by a bom
		self.updateCell(i, j)

	def updateCell(self, i, j):
		#already visited	
		if self.privateBoard[i][j] == -1:			
			return
		if self.publicBoard[i][j] is not None:
			return
		else:
			self.publicBoard[i][j] = 0 


		neighbours = self.getNeighbours(i,j)

		for _i, _j in neighbours:
			if self.privateBoard[_i][_j] == -1:
				self.publicBoard[i][j] += 1
			
		
		if self.publicBoard[i][j] == 0:
			for _i, _j in neighbours:
				self.updateCell(_i, _j)
				

	def getNeighbours(self, i, j):

		potentialNeighbors = [
		(i+1, j),
		(i-1, j),
		(i, j + 1),
		(i, j - 1),
		(i+1, j+1),
		(i+1, j-1),
		(i-1, j-1),
		(i-1, j+1)
		]

		neighbours = []

		for index in range(len(potentialNeighbors)):

			_i, _j = potentialNeighbors[index]

			if _i == -1 or _j == -1:
				continue
			if _i == self.width or _j == self.height:
				continue


			neighbours.append((_i,_j))

		return neighbours


	def toggleFlag(self, cellTuple = None):
		if cellTuple is None:
			i = self.cursor[0]
			j = self.cursor[1]
		else:
			i = cellTuple[0]
			j = cellTuple[1]

		if self.publicBoard[i][j] is None:
			self.publicBoard[i][j] = -1
		elif self.publicBoard[i][j] == -1:
			self.publicBoard[i][j] = None
		else:
			return


	def moveCursor(self, direction):
		i,j = self.cursor

		
		if direction == 'U':
			j-=1
		if direction == 'D':
			j+=1
		if direction == 'L':
			i-=1
		if direction == 'R':
			i+=1

		try:
			self.publicBoard[i][j]
		except IndexError:
			return

		self.cursor = (i,j)
