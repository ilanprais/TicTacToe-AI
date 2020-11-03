import Player

class Human(Player.Player):

	def doTurn(self, board, index):
		if index != None and board.legal(index[0], index[1]) and board.empty(index[0], index[1]):
			board.set(index[0], index[1], self.symbol)
			return True
		else:
			return False
