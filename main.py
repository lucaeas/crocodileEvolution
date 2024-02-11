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
spawnTime = time.time()
limitTime = time.time()
globalMoney = 0
font = pygame.font.SysFont("Arial", 24)
img = font.render(f'Money : {globalMoney}', True, (0,0,0))
activecroco = None
limit = 5

#-----------------------------------------------------------

while running:
    
    #Check if there is any crocodile to spawn
    if time.time() - spawnTime >= 3 and len(listcroco) < limit:
        listcroco.append(Crocodile(screen, 0,random.randint(50,718),random.randint(50,900),False))
        spawnTime = time.time()

    screen.fill((108, 230, 106))

    for croco in listcroco:
        if croco.type != 0:
            if time.time() - croco.ponte > 10:
                globalMoney += croco.money()
                img = font.render(f'Money : {globalMoney}', True, (0,0,0))
                croco.ponte = time.time()
        croco.draw()
    screen.blit(img, (50,70))  
    pygame.draw.rect(screen,(255,255,255),(0,900,768,224))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            for num,e  in enumerate(listcroco):
                if position[0] >= e.x and position[0] <= e.x+100 and position[1] >= e.y and position[1] <= e.y+100 and not e.isHatched():
                    e.setHatched(True)
                    e.type = 1
                    e.ponte = time.time()
                elif position[0] >= e.x and position[0] <= e.x+100 and position[1] >= e.y and position[1] <= e.y+100 and e.isHatched():
                    activecroco = num
                    globalMoney += e.money()
                    img = font.render(f'Money : {globalMoney}', True, (0,0,0))

        if event.type == pygame.MOUSEMOTION:
            
            if activecroco != None:
                rectangleMotion = pygame.Rect(listcroco[activecroco].x,listcroco[activecroco].y,100,100)
                rectangleMotion.move_ip(event.rel)
                listcroco[activecroco].x = rectangleMotion.x
                listcroco[activecroco].y = rectangleMotion.y

        if event.type == pygame.MOUSEBUTTONUP:
            position = event.pos
            if activecroco != None:
                for num, e  in enumerate(listcroco):
                    if num != activecroco:
                        if position[0] >= e.x and position[0] <= e.x+100 and position[1] >= e.y and position[1] <= e.y+100 and e.isHatched() and e.type == listcroco[activecroco].type:
                            e.type += 1
                            listcroco.pop(activecroco)
            activecroco = None
    
    pygame.display.flip()

    mousePos = pygame.mouse.get_pos()

pygame.quit()