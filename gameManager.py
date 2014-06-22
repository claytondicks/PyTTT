'''
Created on Apr 12, 2014

@author: Clayton and Brian
'''


from grid import Grid

class GameManager(object):

	def __init__(self):

		
		self.grid = Grid()

		
	def draw(self, surface):
		
		surface.fill((0,0,0))
		
		for cell in self.grid.getGrid():	
			cell.draw(surface)
	
	
	def getWinner(self):	
		
		for line in self.grid.getMasks():
			noughts = 0
			crosses = 0
			for coord in line:
				if self.grid.getCellState(coord) == 2:
					noughts += 1
				elif self.grid.getCellState(coord) == 1:
					crosses += 1		
			if noughts == 3:
				return "computer"
			elif crosses == 3:
				return "player"
		return None