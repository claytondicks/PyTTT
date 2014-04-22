'''
Created on April 12, 2014

@author: Clayton
'''

import pygame
from display import Display 
from gridManager import GridManager
from player import Player

pygame.init()

screenSize = (320, 318)

surface = pygame.display.set_mode(screenSize)
gridManager = GridManager()
player = Player(gridManager)

display = Display(gridManager)

while True:

	if gridManager.getWinner() == "player":
		print "You Won!"
	elif gridManager.getWinner() == "computer":
		print 'You Lost!'
	else:
		
		player.handleInput()
		display.draw(surface)   
