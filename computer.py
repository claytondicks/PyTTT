'''
Created on Jul 4, 2014

@author: Clayton
'''
from cell import Cell
from option import Option
from random import shuffle

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
	
		shuffle(self.options)
		self.options.sort()
		
		for o in self.options:
			if o.cell.state is None:
				o.cell.setState(Cell.nought)
				return
