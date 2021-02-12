import Tboard
import pygame
import Human
import Robot

WINDOW_SIZE = 600
BACKGROUND_COLOR = (0, 0, 0)
INTERVAL = 50
PLAYER_1_SYMBOL = "X"
PLAYER_2_SYMBOL = "O"

class Tgame():

	def __init__(self, size):
		pygame.init()
		self.size = size
		self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
		self.running = False
		self.set1v1()

	def run(self):
		self.running = True
		self.first = True
		self.board.display(self.screen)
		while self.running:
			self.runFrame()

	def set1v1(self):
		player1 = Human.Human(PLAYER_1_SYMBOL)
		player2 = Human.Human(PLAYER_2_SYMBOL)
		self.board = Tboard.Tboard([player1, player2], self.size, WINDOW_SIZE)

	def set1vAr(self):
		player1 = Human.Human(PLAYER_1_SYMBOL)
		player2 = Robot.Robot(PLAYER_2_SYMBOL, PLAYER_1_SYMBOL)
		self.board = Tboard.Tboard([player1, player2], self.size, WINDOW_SIZE)

	def runFrame(self):
		self.board.setPressZone(None, WINDOW_SIZE)
		self.screen.fill(BACKGROUND_COLOR)

		multiGame = False
		robotGame = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.MOUSEBUTTONUP:
				self.board.setPressZone(pygame.mouse.get_pos(), WINDOW_SIZE)
				multiGame = self.board.multiBtn.isPressed(pygame.mouse.get_pos())
				robotGame = self.board.arBtn.isPressed(pygame.mouse.get_pos())

		self.board.display(self.screen)

		if not self.board.ended() and not self.first:
			self.board.runTurn()
		elif multiGame:
			self.board.restart()
			self.set1v1()
			self.first = False
		elif robotGame:
			self.board.restart()
			self.set1vAr()
			self.first = False
		else:
			self.board.showButtons(self.screen)

		pygame.display.update()
		pygame.time.wait(INTERVAL)

		
