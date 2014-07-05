from cell import Cell

class Option(object):

	def __init__(self, cell):
	
		self.cell = cell
		
	def __lt__(self, other):
		
		if self.cell.state is not None:
			return False
		
		if self.hasTwo(Cell.nought) or self.hasTwo(Cell.cross):
			return True
		
		if self.numEmptyLines() > other.numEmptyLines():
			return True
		
		return False

	def hasTwo(self, player):
		for line in self.cell.solutions:
			if self.count(line)[player] is 2:
				return True
		return False
		
	def numEmptyLines(self):
		counter = 0
		for line in self.cell.solutions:
			c = self.count(line)
			if c[Cell.nought] is 0 and c[Cell.cross] is 0:
				counter += 1
		return counter
			
	def count(self, line):
		count = {}
		count[Cell.nought] = 0
		count[Cell.cross] = 0

		for cell in line:
			if cell.getState() == Cell.nought:
				count[Cell.nought] += 1
			elif cell.getState() == Cell.cross:
				count[Cell.cross] += 1
				
		return count