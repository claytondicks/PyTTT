'''
Created on Apr 12, 2014

@author: Clayton and Brian
'''


from grid import Grid
from cell import Cell

class GameManager(object):

	player = 0
	computer = 1

	def __init__(self):

		self.grid = Grid()

		
	def draw(self, surface):
		
		surface.fill((0,0,0))
		
		for cell in self.grid.getGrid():	
			cell.draw(surface)
	
	
	def getWinner(self):
		winner = self.grid.getWinner()
		if winner is Cell.cross:
			return GameManager.player
		elif winner is Cell.nought:
			return GameManager.computer