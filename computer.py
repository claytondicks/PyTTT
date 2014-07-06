'''
Created on Jul 4, 2014

@author: Clayton
'''
from cell import Cell
from option import Option
from random import shuffle

class Computer(object):
	
	def __init__(self, gameManager):
		self.options = map(Option, gameManager.grid.getGrid())
	
	def turn(self):
	
		shuffle(self.options)
		self.options.sort()
		
		for o in self.options:
			if o.cell.state is None:
				o.cell.setState(Cell.nought)
				return True
				
		return True
		
