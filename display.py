'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame


class Display(object):


	def __init__(self, grid):

		pygame.display.set_caption('Pygame Tic Tac Toe')

		self.grid = grid

	def draw(self, surface):

		self.grid.draw(surface)

		pygame.display.flip()