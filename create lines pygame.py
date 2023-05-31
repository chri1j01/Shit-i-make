import pygame
import sys
import random
from pygame.locals import QUIT
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

temp_var1 = 0
Lines = []

#pygame.draw.line(DISPLAYSURF, green,(10, 10), (10, 990), linelen)
def making_lines():
    for i in range(temp_var1):
        temp_var3 = "pygame.draw.line(DISPLAYSURF, green,Lines[i][0], Lines[i][1], 10)"
        printin_line = eval(temp_var3)
        printin_line

global pos1, pos2, temp
pos1 = (0, 0)
kage = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    mouse_presses = pygame.mouse.get_pressed()



    if event.type == pygame.MOUSEBUTTONDOWN and kage == True:
        
        
            
        kage = False
            
        pos1 = pygame.mouse.get_pos()
    

    if event.type == pygame.MOUSEBUTTONUP:
        kage = True
        
            
        temp = pygame.mouse.get_pos()
        pos2 = (temp[0], temp[1])
        print(pos1, pos2)
        temp_var1 += 1
        Lines.append((pos1, pos2))
            
        
    DISPLAYSURF.fill((255, 255, 255))

   
    making_lines()
    
    pygame.display.update()
    clock.tick(60)
    




