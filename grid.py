'''
Created on Apr 12, 2014

@author: Clayton
'''

import pygame

class Grid(object):

    def __init__(self, surface, player):

        self.image = pygame.image.load('images/grid.png').convert_alpha()
        
        self.surface = surface
        self.player = player

    def draw(self):
        
        self.surface.blit(self.image, (0,0))