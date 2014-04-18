'''
Created on April 12, 2014

@author: Clayton
'''

import pygame
from display import Display 
from grid import Grid
from player import Player

pygame.init()

screenSize = (320, 318)

surface = pygame.display.set_mode(screenSize)
grid = Grid()
player = Player(grid)

display = Display(grid)

while True:

	if grid.getWinner() == "player":
		print "You Won!"
	elif grid.getWinner() == "computer":
		print 'You Lost!'
	else:
		
		player.handleInput()
		display.draw(surface)   
