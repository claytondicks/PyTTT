'''
Created on April 12, 2014

@author: Clayton
'''

import sys
import pygame
from display import Display 

pygame.init()

screenSize = (320, 318)

surface = pygame.display.set_mode(screenSize)

display = Display(surface)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    
    display.draw()
    
    