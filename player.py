'''
Created on Apr 12, 2014

@author: Clayton
'''

import sys
import pygame
from pygame.locals import *

 
class Player(object):
    
    def __init__(self):
        pass
    
	
	
	def handleInput(self):
		
		LEFT = 1
		RIGHT = 3
		
		for event in pygame.event.get():
			
			
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
			elif event.type == MOUSEBUTTONDOWN and event.button == LEFT:
				