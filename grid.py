'''
Created on Apr 19, 2014

@author: Clayton
'''

import pygame
from pygame import Rect
from cell import Cell

class Grid(object):

	def __init__(self):
		self.grid = [None] * 9
		
		
		for row in range(3):
			y = row * (320/3)
			for col in range(3):
				x = col * (320/3)
				
				rect = Rect(y + 5, x + 5, (320/3) - 10, (320/3) - 10)
				self.grid[row * 3 + col] = Cell(rect)

		
	def getMasks(self):
		row1 = [(5,5), (111, 5), (217,5)]
		row2 = [(5,111), (111, 111), (217,111)]
		row3 = [(5,217), (111, 217), (217,217)]
		
		col1 = [(5,5), (5, 111), (5,212)]
		col2 = [(111,5), (111, 111), (111,5)]
		col3 = [(217,5), (217, 106), (217,217)]
		
		diag1 = [(5,5), (111, 111), (217,217)]
		diag2 = [(5,217), (111, 111), (217,5)]
		
		return row1, row2, row3, col1, col2, col3, diag1, diag2
	
	
	def getGrid(self):
		return self.grid
	
	
	def getCellState(self, pos):
		for cell in self.grid:
			if cell.isClicked(pos):
				return cell.getState()
			
		return 0	