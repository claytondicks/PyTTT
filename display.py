'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame


class Display(object):


    def __init__(self, surface):
        
        self.surface = surface
        self.image= pygame.image.load('images/grid.png').convert_alpha()
        
        pygame.display.set_caption('Pygame Tic Tac Toe')
        
        
    def draw(self):
        
        self.surface.blit(self.image, (0,0))
        
        pygame.display.flip()