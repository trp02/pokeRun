import pygame, sys, random

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 675

class Model:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jump = False
        self.velocity = 10
        

    
class obstacle1(Model):
    
    img = pygame.image.load("assets/spike1.png")
    #returns image and x, y coords 
    def getImgInfo(self):
        return (self.img, self.x, self.y)
    
    def getHitbox(self):
        return (self.x + 10, self.y + 8, self.width - 16, self.height - 3)
    
class obstacle2(Model):

    img = pygame.image.load("assets/spike2.png")
    #returns image and x, y coords 
    def getImgInfo(self):
        return (self.img, self.x, self.y)
    def getHitbox(self):
        return (self.x + 8, self.y + 3, self.width - 12, self.height - 3)
    
    
class character(Model):
    
    #walking animation
    charwalk = [pygame.image.load("assets/bulbasaur/walk1.png"), pygame.image.load("assets/bulbasaur/walk2.png"), pygame.image.load("assets/bulbasaur/walk3.png"), pygame.image.load("assets/bulbasaur/walk4.png")]
    charjump = pygame.image.load("assets/bulbasaur/jump.png")
    walk = 0
    animation_timer = 0
    animation_delay = 20 # Animation delay 
    current_time = 0
    def getImgInfo(self):
        self.current_time += 1
        if self.current_time - self.animation_timer > self.animation_delay:
            self.walk += 1
            # Reset the walk counter if it exceeds the length of the charwalk list
            if self.walk >= len(self.charwalk):
                self.walk = 0
            # Update the animation timer
            self.animation_timer = self.current_time
        # return image info
        if self.jump == True:
            return (self.charjump, self.x, self.y)
        return (self.charwalk[self.walk], self.x, self.y)
    
    #gets hitbox for character. A little smaller than what you see to allow for some on-the-edge gameplay
    def getHitbox(self):
        return (self.x + 13, self.y + 25, self.width - 30, self.height - 40)
