from cell import Cell

class Option(object):

	def __init__(self, cell):
	
		self.cell = cell
		
	def __lt__(self, other):
		
		if self.cell.state is not None:
			return False

		if self.hasTwo(Cell.nought):
			return True
			
		if self.hasTwo(Cell.cross):
			return True
		
		if other.hasTwo(Cell.nought):
			return False
			
		if other.hasTwo(Cell.cross):
			return False
		
		if self.numEmptyLines() > other.numEmptyLines():
			return True

		if self.numAvailable() > other.numAvailable():
			return True

		return False

	def numAvailable(self):
		counter = 0
		for line in self.cell.solutions:
			c = self.count(line)
			if c[Cell.nought] == 1 and c[Cell.cross] == 0:
				counter += 1
		return counter
		
	def hasTwo(self, player):
		for line in self.cell.solutions:
			c = self.count(line)
			if c[player] is 2 and c[not player] is 0:
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
