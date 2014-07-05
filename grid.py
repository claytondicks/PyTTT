'''
Created on Apr 19, 2014

@author: Clayton
'''

import pygame
from pygame import Rect
from cell import Cell

class Grid(object):

	lines = []
	lines.append([0, 1, 2])
	lines.append([3, 4, 5])
	lines.append([6, 7, 8])
	lines.append([0, 3, 6])
	lines.append([1, 4, 7])
	lines.append([2, 5, 8])
	lines.append([0, 4, 8])
	lines.append([6, 4, 2])

	def __init__(self):
		self.grid = [None] * 9
		
		for row in range(3):
			y = row * (320/3)
			for col in range(3):
				x = col * (320/3)
				
				rect = Rect(y + 5, x + 5, (320/3) - 10, (320/3) - 10)
				index = row * 3 + col
				
				self.grid[index] = Cell(rect)
		

		for i in range(len(self.grid)):
			solutions = []
			for line in Grid.lines:
				if i in line:
					solutions.append((self.grid[line[0]], self.grid[line[1]], self.grid[line[2]]))
			self.grid[i].solutions = solutions
			
	def getWinner(self):
		for line in Grid.lines:
			winner = self.winnerForLine(line)
			if winner is not None:
				return winner
	
	def winnerForLine(self, line):
		cellstates = map(lambda cell: self.grid[cell].getState(), line)
		if None in cellstates:
			return None
		if Cell.nought in cellstates and Cell.cross not in cellstates:
			return Cell.nought
		if Cell.cross in cellstates and Cell.nought not in cellstates:
			return Cell.cross

	def getGrid(self):
		return self.grid
