'''
Created on Jul 4, 2014

@author: Clayton
'''
from cell import Cell
from option import Option

class Computer(object):
	
	def __init__(self, gameManager):
		self.theGame = gameManager
		
		self.grid = self.theGame.grid.getGrid()
		self.options = map(Option, self.grid)

				
	def placeNought(self, line):
	
		for cell in line:
			if cell.getState() == None:
				cell.setState(Cell.nought)
				break
		
	
	def move(self):

		self.options.sort()
		top = self.options[0]
		top.cell.setState(Cell.nought)
