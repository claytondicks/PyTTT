'''
Created on Apr 12, 2014

@author: Clayton and Brian
'''

import pygame
from utils import *

class GridManager(object):

	def __init__(self):

		
		self.theGrid = GridManager()

		
	def draw(self, surface):
		
		surface.fill((0,0,0))
		
		for cell in self.getCells():	
			cell.draw(surface)
	
	
	def getWinner(self):
		
		for i in range(3):	
			#checks each row for a winner
			newGrid = [row[i] for row in self.theGrid]	
			if checkEqual(newGrid):
				return "player"
		
			#Checks the columns
			if checkEqual(self.theGrid[i]):
				return "player"
		
		
		return None