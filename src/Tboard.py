import Board
import Button
import pygame

CELL_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 0, 0)
BANNER_HEIGHT = 30
BUTTON_WIDTH = 70

class Tboard():

	def __init__(self, players, size, screenSize):
		self.board = Board.Board(size)
		self.size = size
		self.players = players
		self.current = 0
		self.pressedZone = None
		self.multiBtn = Button.Button(screenSize - 3 * BUTTON_WIDTH, 0, BUTTON_WIDTH, BANNER_HEIGHT, BUTTON_COLOR, "1 v 1", CELL_COLOR) 
		self.arBtn = Button.Button(screenSize - 4.5 * BUTTON_WIDTH, 0, 1.2 * BUTTON_WIDTH, BANNER_HEIGHT, BUTTON_COLOR, "1 v AI", CELL_COLOR) 

	def restart(self):
		self.board = Board.Board(self.size)
		self.current = 0
		self.pressedZone = None

	def runTurn(self):
		if self.players[self.current].doTurn(self.board, self.pressedZone):
			self.switchPlayer()

	def switchPlayer(self):
		self.current = (self.current + 1) % len(self.players)

	def winner(self):
		for player in self.players:
			for r in range(self.size):
				if self.lineEq(r, 0, 0, 1, player.symbol):
					return player
			for r in range(self.size):
				if self.lineEq(0, r, 1, 0, player.symbol):
					return player
			if self.lineEq(0, 0, 1, 1, player.symbol):
					return player
			if self.lineEq(self.size - 1, 0, -1, 1, player.symbol):
					return player
		return None

	def ended(self):
		return self.board.full() or self.winner() != None

	def lineEq(self, startRow, startCol, rowJump, colJump, symbol):
		i = startRow
		j = startCol
		while i < self.size and j < self.size:
			if not self.board.get(i, j) == symbol:
				return False
			i += rowJump
			j += colJump

		return True

	def setPressZone(self, pos, screenSize):
		zone = None
		cellSize = int(screenSize / self.size)
		if not pos == None:
			index = [int(pos[0]/cellSize), int(pos[1]/cellSize)]
			if index[0] < self.size and index[1] < self.size and index[0] >= 0 and index[1] >= 0:
				zone = index
		self.pressedZone = zone

	def showButtons(self, surface):
		self.multiBtn.display(surface)
		self.arBtn.display(surface)
		
	def display(self, surface):
		pygame.font.init() 
		cellSize = int(surface.get_width()/self.size)

		# fonts
		large = pygame.font.SysFont('Comic Sans MS', cellSize)
		text = pygame.font.SysFont('Comic Sans MS', int(1.2*BANNER_HEIGHT))

		# Top banner
		pygame.draw.rect(surface, CELL_COLOR, pygame.Rect((0, 0), (surface.get_width(), BANNER_HEIGHT)))
		turn = text.render("Player: " + self.players[self.current].symbol, False, (0, 0, 0))
		surface.blit(turn, (int(BANNER_HEIGHT / 10), int(BANNER_HEIGHT / 10)))

		# Winner
		winner = self.winner()
		if not winner == None:
			winText = text.render("Winner: " + winner.symbol, False, (0, 0, 0))
			surface.blit(winText, (int(surface.get_width() - 120), int(BANNER_HEIGHT / 10)))
		elif self.board.full():
			winText = text.render("Draw ", False, (0, 0, 0))
			surface.blit(winText, (int(surface.get_width() - 70), int(BANNER_HEIGHT / 10)))

		for x in range(self.size):
			if x > 0:
				# lines
				pygame.draw.line(surface, CELL_COLOR, (x*cellSize, 0), (x*cellSize, surface.get_width()))
				pygame.draw.line(surface, CELL_COLOR, (0, x*cellSize), (surface.get_width(), x*cellSize))
			for y in range(self.size):
				symbol = large.render(self.board.get(x, y), False, CELL_COLOR)
				surface.blit(symbol,(int(x*cellSize + cellSize/4), int(y*cellSize + cellSize/4)))

	def __str__(self):
		return self.board.__str__()
