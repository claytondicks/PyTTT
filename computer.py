'''
Created on Jul 4, 2014

@author: Clayton
'''
from cell import Cell


class Computer(object):
	
	def __init__(self, gameManager):
		self.theGame = gameManager
	
	
	
	def move(self):
		for cell in self.theGame.grid.getGrid():
			if cell.getState() == None:
				cell.setState(Cell.nought)
				break