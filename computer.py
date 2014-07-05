'''
Created on Jul 4, 2014

@author: Clayton
'''
from cell import Cell


class Computer(object):
	
	def __init__(self, gameManager):
		self.theGame = gameManager
		
		self.grid = self.theGame.grid.getGrid()
		

	def count(self, line):
		computer = 0
		player = 0
		empty = 0
		
		
		for cell in line:
			if cell.getState() == Cell.nought:
				computer += 1			
			elif cell.getState() == Cell.cross:
				player += 1
			else:
				empty += 1
				
		return computer, player, empty
				
	def placeNought(self, line):
	
		for cell in line:
			if cell.getState() == None:
				cell.setState(Cell.nought)
				break
		
	
	def move(self):

		lines = self.theGame.grid.lines
		
		for line in lines:
			cellstates = map(lambda cell: self.grid[cell], line)
			
			computer, player, empty = self.count(cellstates)
			
			if player == 2 and empty == 1:
				self.placeNought(cellstates)
				return
			elif computer == 2 and empty == 1:
				self.placeNought(cellstates)
				return
			elif computer == 0 and empty == 2:
				self.placeNought(cellstates)
				return
			
			