'''
Created on April 12, 2014

@author: Clayton
'''

import sys
import pygame
from display import Display 
from grid import Grid
from player import Player

pygame.init()

screenSize = (320, 318)

surface = pygame.display.set_mode(screenSize)
grid = Grid()
player = Player(grid)

display = Display(grid, player)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    
	player.handleInput()
	display.draw(surface)   
    