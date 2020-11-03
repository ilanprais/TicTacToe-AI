BLANK = " "

class Board():
	
	def __init__(self, size):
		self.grid = []
		self.size = size
		for i in range(size):
			inner = []
			for j in range(size):		
				inner.append(BLANK)
			self.grid.append(inner)

	def set(self, row, col, val):
		self.grid[row][col] = val

	def get(self, row, col):
		return self.grid[row][col]

	def empty(self, row, col):
		return self.grid[row][col] == BLANK

	def full(self):
		for i in range(self.size):
			for j in range(self.size):
				if self.empty(i, j):
					return False
		return True


	def legal(self, row, col):
		return row >=0 and col >=0 and row < self.size and col < self.size

	def __str__(self):
		string = ""
		for i in range(self.size):
			for j in range(self.size):	
				string += "|" + str(self.grid[i][j])
			string += "|\n"
		return string


		
		