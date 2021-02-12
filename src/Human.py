import Player

class Human(Player.Player):

	def doTurn(self, tboard, index):
		if index != None and tboard.board.legal(index[0], index[1]) and tboard.board.empty(index[0], index[1]):
			tboard.board.set(index[0], index[1], self.symbol)
			return True
		else:
			return False
