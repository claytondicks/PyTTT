'''
Created on April 12, 2014

@author: Clayton
'''

import pygame
pygame.init()
screenSize = (320, 318)
surface = pygame.display.set_mode(screenSize)


from display import Display 
from gameManager import GameManager
from player import Player


gameManager = GameManager()
player = Player(gameManager)

display = Display(gameManager)

winner = None
clock = pygame.time.Clock()

while winner is None:

	clock.tick(30)

	player.handleInput()
	display.draw(surface)
	
	winner = gameManager.getWinner()
		

if winner is GameManager.player:
	print "You Won!"
else:
	print 'You Lost!'