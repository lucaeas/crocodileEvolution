import pygame
    
class Crocodile:
    
    def __init__(self, win, type,x,y,hatched):
        self.win = win
        self.type = type
        self.x = x
        self.y = y
        self.hatched = hatched

    def money(self):
        if self.type == 1:
            return 1
        else:
            return 3

    def isHatched(self):
        return self.hatched   

    def setHatched(self,state: bool):
        self.hatched = state

    def getPos(self):
        return(self.x,self.y)
    
    def draw(self):
        if self.isHatched():
            pygame.draw.rect(self.win,(0, 92, 17),pygame.Rect(self.x,self.y,50,50),0)
        else:
            pygame.draw.rect(self.win,(191, 138, 92),pygame.Rect(self.x,self.y,50,50),0)

    def __repr__(self):
        return f"{self.x},{self.y},{self.type}"