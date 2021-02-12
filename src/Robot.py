import Player
import Tminmax

class Robot(Player.Player):

	def __init__(self, symbol, opSymbol):
		super().__init__(symbol)
		self.minmax = Tminmax.Tminmax(symbol, opSymbol)

	def doTurn(self, tboard, index):
		move = self.minmax.bestMove(tboard)
		print(move)
		if not move == None:
			tboard.board.set(move[0], move[1], self.symbol)
			return True
		return False

		