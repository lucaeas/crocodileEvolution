import pygame
import random
import time
probabebi = [1 for _ in range(9)] + [3]
probakasket = [1 for _ in range(3)] + [3 for _ in range(7)]
probapirate = [3 for _ in range(3)] + [5 for _ in range(6)] + [10]
class Crocodile:
    
    def __init__(self, win, type,x,y,hatched,ponte=0):
        self.win = win
        self.type = type
        self.x = x
        self.y = y
        self.hatched = hatched
        self.ponte = ponte

    def money(self):
        if self.type == 1:
            return random.choice(probabebi)
        elif self.type == 2:
            return random.choice(probakasket)
        elif self.type == 3:
            return random.choice(probapirate)

    def isHatched(self):
        return self.hatched   

    def setHatched(self,state: bool):
        self.hatched = state

    def getPos(self):
        return(self.x,self.y)
    
    def draw(self):
            if self.type == 0:
                image = pygame.image.load("images/egg.png").convert_alpha()
            elif self.type == 1:
                image = pygame.image.load("images/bebicroco.png").convert_alpha()
            elif self.type == 2:
                image = pygame.image.load("images/kasketcroco.png").convert_alpha()
            elif self.type == 3:
                image = pygame.image.load("images/piratecroco.png").convert_alpha()
            image = pygame.transform.scale(image, (100, 120))
            self.win.blit(image, (self.x,self.y))

    def __repr__(self):
        return f"{self.x},{self.y},{self.type}"