'''
Created on Apr 19, 2014

@author: Clayton
'''

import pygame
from pygame import Rect
from cell import Cell

class GridManager(object):

	def __init__(self):
		self.theGrid = [None] * 3
		
		self.buildGrid()
		
	def buildGrid(self):
		cells = [None] * 3

		for row in range(3):
			y = row * (320/3)
			for col in range(3):
				x = col * (320/3)
				rect = Rect(y + 5, x + 5, (320/3) - 10, (320/3) - 10)
		
				cells[col] = Cell(rect)
		
			self.theGrid[row] = cells
			cells = [None] * 3
		
	
	def getCells(self):
		cells = [None] * 9
		for rows in self.theGrid:	
			for col_index, cell in enumerate(rows):
				cells[col_index].append(cell)
				
		return cells
	
	def getLines(self):
		pass
	
	def get_rows(self):
		return [[cell for cell in row] for row in self.theGrid]

	def get_cols(self):
		cols = [None] * 3
		for row in self.theGrid:
			for col_index, cell in enumerate(row):
				cols[col_index].append(cell)
		return cols 
	
	def get_diag(self):
		diag = [None] * 2
		l = len(self.theGrid[0])
		diag += [self.theGrid[i][i] for i in range(l)]              
		diag += [self.theGrid[l-1-i][i] for i in range(l-1,-1,-1)]
		
		return diag