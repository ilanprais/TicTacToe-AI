import pygame

class Button():

	def __init__(self, x, y, width, height, color, text, textColor):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.text = text
		self.textColor = textColor
		self.rect = pygame.Rect((x, y), (width, height))

	def display(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)
		font = pygame.font.SysFont('Comic Sans MS', int(1.2*self.height))
		text = font.render(self.text, False, self.textColor)
		surface.blit(text, (self.x  + 10, self.y))

	def isPressed(self, pos):
		return pos[0] > self.x and pos[1] > self.y and pos[0] < self.x + self.width and pos[1] < self.y + self.height