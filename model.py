import pygame, sys, random

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 675

class Model:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 10, self.y, 28, 315)

        
class obstacle1(Model):
    
    img = pygame.image.load("assets/spike1.png")
    #returns image and x, y coords 
    def getImgInfo(self):
        return (self.img, self.x, self.y)
    
class obstacle2(Model):

    img = pygame.image.load("assets/spike2.png")
    #returns image and x, y coords 
    def getImgInfo(self):
        return (self.img, self.x, self.y)
