'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame
from pygame.color import THECOLORS


class Display(object):


    def __init__(self, surface):
        
        self.surface = surface
        
        pygame.display.set_caption('Pygame Tic Tac Toe')
        
        
    def draw(self):
        
        self.surface.fill(THECOLORS["cornflowerblue"])
        
        pygame.display.flip()