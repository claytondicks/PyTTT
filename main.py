'''
Created on April 12, 2014

@author: Clayton
'''

import pygame
from display import Display 
from gameManager import GameManager
from player import Player

pygame.init()

screenSize = (320, 318)

surface = pygame.display.set_mode(screenSize)
gameManager = GameManager()
player = Player(gameManager)

display = Display(gameManager)

while True:

	if gameManager.getWinner() == "player":
		print "You Won!"
	elif gameManager.getWinner() == "computer":
		print 'You Lost!'
	else:
		
		player.handleInput()
		display.draw(surface)   
