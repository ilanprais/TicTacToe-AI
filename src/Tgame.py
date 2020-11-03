import Tboard
import pygame
import Human

WINDOW_SIZE = 600
BACKGROUND_COLOR = (0, 0, 0)
INTERVAL = 50
PLAYER_1_SYMBOL = "X"
PLAYER_2_SYMBOL = "O"

class Tgame():

	def __init__(self, size):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
		player1 = Human.Human(PLAYER_1_SYMBOL)
		player2 = Human.Human(PLAYER_2_SYMBOL)
		self.board = Tboard.Tboard([player1, player2], 3, WINDOW_SIZE)
		self.running = False

	def run(self):
		self.running = True
		self.first = True
		self.board.display(self.screen)
		while self.running:
			self.runFrame()

	def runFrame(self):
		self.board.setPressZone(None, WINDOW_SIZE)
		self.screen.fill(BACKGROUND_COLOR)

		newGame = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.MOUSEBUTTONUP:
				self.board.setPressZone(pygame.mouse.get_pos(), WINDOW_SIZE)
				newGame = self.board.multiBtn.isPressed(pygame.mouse.get_pos())

		self.board.display(self.screen)

		if not self.board.ended() and not self.first:
			self.board.runTurn()
		elif newGame:
		 	self.board.restart()
		 	self.first = False
		else:
			self.board.showButtons(self.screen)

		pygame.display.update()
		pygame.time.wait(INTERVAL)

		
