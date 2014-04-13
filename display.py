'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame
from grid import Grid


class Display(object):


    def __init__(self, surface, player):
        
        self.surface = surface
        self.player = player        
        
        pygame.display.set_caption('Pygame Tic Tac Toe')
        
        self.grid = Grid(self.surface, self.player)
        
        
    def draw(self):
        
        self.grid.draw()
                
        pygame.display.flip()