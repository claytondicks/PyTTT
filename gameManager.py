'''
Created on Apr 12, 2014

@author: Clayton and Brian
'''


from grid import Grid
from cell import Cell
from player import Player
from computer import Computer

class GameManager(object):

	def __init__(self):
		self.grid = Grid()
		self.players = {}
		self.players[Cell.cross] = Player(self)
		self.players[Cell.nought] = Computer(self)
		self.turn = Cell.cross
		
	def doTurn(self):
	
		if self.players[self.turn].turn():
			self.turn = not self.turn
			return self.getWinner()

		return None
		
	def draw(self, surface):
		
		surface.fill((0,0,0))
		
		for cell in self.grid.getGrid():	
			cell.draw(surface)
	
	def getWinner(self):
		return self.grid.getWinner()