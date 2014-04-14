'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame
from grid import Grid


class Display(object):


    def __init__(self, player):
        
        self.player = player        
        
        pygame.display.set_caption('Pygame Tic Tac Toe')
        
        self.grid = Grid(self.player)
        
        
    def draw(self, surface):
        
        self.grid.draw(surface)
                
        pygame.display.flip()