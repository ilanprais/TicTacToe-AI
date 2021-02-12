import Minmax
import Board
import copy

VALUE = 10

class Tminmax(Minmax.Minmax):

	def __init__(self, maximizer, minimizer):
		super().__init__()
		self.maximizer = maximizer
		self.minimizer = minimizer

	def updateStructre(self, structre, move, isMaximizer):
		if isMaximizer:
			structre.board.set(move[0], move[1], self.maximizer)
		else:
			structre.board.set(move[0], move[1], self.minimizer)


	def resetStructre(self, structre, move):
		structre.board.set(move[0], move[1], Board.BLANK)

	def evaluate(self, structre):
		if not structre.winner() == None:
			if structre.winner().symbol == self.maximizer:
				return VALUE
			else:
				return -1*VALUE
		return 0

	def moves(self, structre):
		empty = []
		for i in range(structre.size):
			for j in range(structre.size):
				if structre.board.empty(i, j):
					empty.append([i, j])
		return empty



