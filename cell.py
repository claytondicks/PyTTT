'''
Created on Apr 13, 2014

@author: Clayton
'''
import pygame


class Cell(object):
	'''
	classdocs
	'''
	nought = False
	cross = True

	fill = {}
	fill[nought] = pygame.image.load("images/o.png").convert_alpha()
	fill[cross] = pygame.image.load("images/x.png").convert_alpha()
	
	def __init__(self, rect):
		'''
		Constructor
		'''
		self.rect = rect
		self.state = None
		
		self.width = self.rect.width
		self.height = self.rect.height

		self.cellSurface = pygame.Surface((self.width , self.height))
		
	
	def getState(self):
		return self.state
	
	def setState(self, state):
		if self.state == None:
			self.state = state
	
	def __eq__(self, cell):
		if self.getState() == cell.getState() and self.getState() is not None:
			return True
		else:
			return False
	
	def draw(self, surface):
			
		if self.state not in Cell.fill:
			self.cellSurface.fill((255,255,255))
		else:
			self.cellSurface.blit(Cell.fill[self.state], (0,0))

		surface.blit(self.cellSurface, (self.rect.left, self.rect.top))
		
	def isClicked(self, point):
		return self.rect.collidepoint(point)