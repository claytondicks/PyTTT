'''
Created on April 12, 2014

@author: Clayton
'''

import pygame
from display import Display 

pygame.init()

screenSize = (600, 600)

surface = pygame.display.set_mode(screenSize)

display = Display(surface)

while True:
    
    display.draw()