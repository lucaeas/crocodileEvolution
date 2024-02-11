import pygame
import math
import random
import time
from croco import *

pygame.init()
screen = pygame.display.set_mode((768, 1024))
pygame.display.set_caption("Croco Evolution")

#-----------------------------------------------------------
listcroco = []
running = True
firstTime = time.time()
globalMoney = 0
font = pygame.font.SysFont("Arial", 72)
img = font.render(f'Money : {globalMoney}', True, (0,0,0))
activecroco = None

#-----------------------------------------------------------

while running:
    
    if time.time() - firstTime >= 1 and len(listcroco) < 5:
        listcroco.append(Crocodile(screen, 1,random.randint(50,718),random.randint(50,974),False))
        firstTime = time.time()

    screen.fill((108, 230, 106))
    for croco in listcroco:
        croco.draw()
    screen.blit(img, (50,50))    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            for num,e  in enumerate(listcroco):
                if position[0] >= e.x and position[0] <= e.x+50 and position[1] >= e.y and position[1] <= e.y+50 and not e.isHatched():
                    e.setHatched(True)
                elif position[0] >= e.x and position[0] <= e.x+50 and position[1] >= e.y and position[1] <= e.y+50 and e.isHatched():
                    activecroco = num
                    globalMoney += e.money()
                    img = font.render(f'Money : {globalMoney}', True, (0,0,0))

        if event.type == pygame.MOUSEMOTION:
            
            if activecroco != None:
                rectangleMotion = pygame.Rect(listcroco[activecroco].x,listcroco[activecroco].y,50,50)
                rectangleMotion.move_ip(event.rel)
                listcroco[activecroco].x = rectangleMotion.x
                listcroco[activecroco].y = rectangleMotion.y

        if event.type == pygame.MOUSEBUTTONUP:
            activecroco = None
    
    pygame.display.flip()

    mousePos = pygame.mouse.get_pos()

pygame.quit()