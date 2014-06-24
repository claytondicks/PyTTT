'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame


class Display(object):


	def __init__(self, gameManager):

		pygame.display.set_caption('Pygame Tic Tac Toe')
		self.theGame = gameManager

	def draw(self, surface):

		self.theGame.draw(surface)

		pygame.display.flip()
