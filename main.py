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
from computer import Computer


gameManager = GameManager()
player = Player(gameManager)
computer = Computer(gameManager)

display = Display(gameManager)

winner = None
clock = pygame.time.Clock()

playerTurn = True


while winner is None:

	clock.tick(30)

	if playerTurn:
		if player.handleInput():
			winner = gameManager.getWinner()
			playerTurn = False
		
	if not playerTurn:
		computer.move()
		winner = gameManager.getWinner()
		playerTurn = True
		
	display.draw(surface)	
	
		

if winner is gameManager.player:
	print "You Won!"
else:
	print 'You Lost!'