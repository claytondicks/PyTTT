'''
Created on Apr 13, 2014

@author: Clayton
'''
from pygame import Rect



class Cell(object):
    '''
    classdocs
    '''

    def __init__(self, rect, surface):
        '''
        Constructor
        '''
        
        self.rect = rect
        self.state = 0
        
        
    def getState(self):
        return self.state
    
    def draw(self):
        return self.rect
                