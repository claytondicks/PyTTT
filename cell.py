'''
Created on Apr 13, 2014

@author: Clayton
'''
import pygame


class Cell(object):
	'''
	classdocs
	'''

	def __init__(self, rect):
		'''
		Constructor
		'''
		
		self.rect = rect
		
		#State 0 is blank, 1 is a Cross and 2 is a Naught
		self.state = 0
		
		self.width = self.rect.width
		self.height = self.rect.height
		
		self.cellsurface = pygame.Surface((self.width , self.height))
		
		self.cross = pygame.image.load("images/x.png").convert_alpha()
		self.naught = pygame.image.load("images/o.png").convert_alpha()
	
	
	def getState(self):
		return self.state
	
	
	def setState(self, state):
		if self.state == 0:
			self.state = state
			
	
	def draw(self, surface):
			
		if self.state == 0:
			self.cellsurface.fill((255,255,255))	
	
		if self.state == 1:		
			self.cellsurface.blit(self.cross, (0,0))
		
		if self.state == 2:		
			self.cellsurface.blit(self.naught, (0,0))

		
		surface.blit(self.cellsurface, (self.rect.left, self.rect.top))


	def isClicked(self, point):
	
		return self.rect.collidepoint(point)