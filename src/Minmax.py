
class Minmax():

	def __init__(self):
		self.track = 0

	def bestMove(self, board):
		bestMove = self.moves(board)[0]
		bestVal = -1*float("inf")
		for move in self.moves(board):
			self.updateStructre(board, move, 1)
			val = self.minimax(board, 0, False)
			self.resetStructre(board, move)
			if val > bestVal:
				bestVal = val
				bestMove = move
		return bestMove

	def minimax(self, structre, depth, isMaximizing):

		eval = self.evaluate(structre)

		if eval > 0:
			return eval

		if eval < 0:
			return eval

		if len(self.moves(structre)) == 0:
			return 0

		if isMaximizing:
			bestVal = -1*float("inf")
			for move in self.moves(structre):
				self.updateStructre(structre, move, isMaximizing)
				value = self.minimax(structre, depth + 1, not isMaximizing)
				bestVal = self.max(bestVal, value)
				self.resetStructre(structre, move)

			return bestVal

		else:
			bestVal = float("inf")
			for move in self.moves(structre):
				self.updateStructre(structre, move, isMaximizing)
				value = self.minimax(structre, depth + 1, not isMaximizing)
				bestVal = self.min(bestVal, value)
				self.resetStructre(structre, move)

			return bestVal

	def max(self, a, b):
		if a > b:
			return a
		return b

	def min(self, a, b):
		if a < b:
			return a
		return b

	def updatedStructre(self, structre, move):
		pass

	def evaluate(self, structre):
		pass

	def moves(self, structre):
		pass
