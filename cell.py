'''
Created on Apr 13, 2014

@author: Clayton
'''
import pygame


class Cell(object):
    '''
    classdocs
    '''

    def __init__(self, rect):
        '''
        Constructor
        '''
        
        self.rect = rect
        self.state = 0
        
        self.width = self.rect.width
        self.height = self.rect.height
        
        self.cellsurface = pygame.Surface((self.width , self.height))
        
        
    def getState(self):
        return self.state
    
    
    def draw(self, surface):
        
        self.cellsurface.fill((255,255,255))
        
        surface.blit(self.cellsurface, (self.rect.left, self.rect.top))
                