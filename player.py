'''
Created on Apr 12, 2014

@author: Clayton
'''

import sys
import pygame
from pygame.locals import *


class Player(object):

	def __init__(self, grid):
		self.grid = grid
	
	
	
	def handleInput(self):
		
		LEFT = 1
		
		for event in pygame.event.get():
		
			pos = pygame.mouse.get_pos()
			
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
			elif event.type == MOUSEBUTTONDOWN and event.button == LEFT:
				for cell in self.grid.getCells():
						if cell.isClicked(pos):
							cell.setState(1)