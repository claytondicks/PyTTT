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

turn = 0


while winner is None:

	clock.tick(30)

	if turn == 0:
		if player.handleInput():
			turn = 1
		
	if turn == 1:
		computer.move()
		turn = 0
		
	display.draw(surface)	
	winner = gameManager.getWinner()
		

if winner is gameManager.player:
	print "You Won!"
else:
	print 'You Lost!'