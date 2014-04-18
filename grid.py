'''
Created on Apr 12, 2014

@author: Clayton and Brian
'''

import pygame
from pygame.rect import Rect
from cell import Cell
from utils import *

class Grid(object):

	def __init__(self):

		
		self.theGrid = self.buildGrid()

		
	def draw(self, surface):
		
		surface.fill((0,0,0))
		
		for cell in self.getCells():	
			cell.draw(surface)
	
	
	def buildGrid(self):
		cells = [None] * 3
		theGrid = [None] * 3
		
		for row in range(3):
			y = row * (320/3)
			for col in range(3):
				x = col * (320/3)
				rect = Rect(y + 5, x + 5, (320/3) - 10, (320/3) - 10)
				
				cells[col] = Cell(rect)
			
			theGrid[row] = cells
			cells = [None] * 3
			
		return theGrid  
					
	
	def getCells(self):
		cells = [None] * 9
		count = 0
		for rows in self.theGrid:	
			for cell in rows:
				cells[count] = cell
				count += 1
				
		return cells
	
	
	def getWinner(self):		
		if checkEqual(self.theGrid[0]):
			return "player"
		
		return None