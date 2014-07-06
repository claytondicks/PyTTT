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

gameManager = GameManager()
display = Display(gameManager)

clock = pygame.time.Clock()

winner = None
while winner is None:
	clock.tick(30)
	winner = gameManager.doTurn()
	display.draw(surface)	

if winner:
	print "You Won!"
else:
	print 'You Lost!'