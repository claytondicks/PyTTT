'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame
from pygame.rect import Rect
from random import randint

class Grid(object):

	def __init__(self, surface, player):

		self.grid = [None] * 9

		for row in range(3):
			y = row * (320/3)
			for col in range(3):
				x = col * (320/3)
				self.grid[row * 3 + col] = (Rect(y + 5, x + 5, (320/3) - 10, (320/3) - 10), 0)
			
		self.surface = surface
		self.player = player

	def draw(self):
		
		self.surface.fill((0,0,0))
		
		for cell in self.grid:
			
			color = (randint(0,255),randint(0,255),randint(0,255))
			
			self.surface.fill(color, cell[0])
		
