'''
Created on Apr 12, 2014

@author: Clayton and Brian
'''

import pygame
from pygame.rect import Rect
from cell import Cell

class Grid(object):

	def __init__(self):

		self.cells = [None] * 9

		for row in range(3):
			y = row * (320/3)
			for col in range(3):
				x = col * (320/3)
				rect = Rect(y + 5, x + 5, (320/3) - 10, (320/3) - 10)
				
				self.cells[row * 3 + col] = Cell(rect)


	def draw(self, surface):
		
		surface.fill((0,0,0))
		
		for cell in self.cells:	
			cell.draw(surface)