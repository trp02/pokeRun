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
        self.curChar = 0

class snorObs(Model):
    snorImg = [pygame.image.load("assets/fatass/sleep1.png"),pygame.image.load("assets/fatass/sleep2.png") ]
    
    animation_timer = 0
    animation_delay = 20 # Animation delay 
    current_time = 0
    frame = 0
    def getImgInfo(self):
        self.current_time += 1
        if self.current_time - self.animation_timer > self.animation_delay:
            self.frame += 1
            # Reset the walk counter if it exceeds the length of the charwalk list
            if self.frame >= len(self.snorImg):
                self.frame = 0
            # Update the animation timer
            self.animation_timer = self.current_time
        # return image info
    
        return (self.snorImg[self.frame], self.x, self.y)
    
    def getHitbox(self):
        return (self.x + 29, self.y+10, self.width -30, self.height)
    
class grassObs(Model):
    grassImg = [pygame.image.load("assets/grass/tree2.png"),pygame.image.load("assets/grass/tree2.png")]
    
    animation_timer = 0
    animation_delay = 20 # Animation delay 
    current_time = 0
    frame = 0
    def getImgInfo(self):
        self.current_time += 1
        if self.current_time - self.animation_timer > self.animation_delay:
            self.frame += 1
            # Reset the walk counter if it exceeds the length of the charwalk list
            if self.frame >= len(self.grassImg):
                self.frame = 0
            # Update the animation timer
            self.animation_timer = self.current_time
        # return image info
    
        return (self.grassImg[self.frame], self.x, self.y)
    
    def getHitbox(self):
        return (self.x + 30, self.y + 30, self.width +20, self.height - 90)

class fireObs(Model):
    fireImg = [pygame.image.load("assets/fire/fire1.png"),pygame.image.load("assets/fire/fire2.png"), pygame.image.load("assets/fire/fire3.png"),pygame.image.load("assets/fire/fire4.png")]
    
    animation_timer = 0
    animation_delay = 10 # Animation delay 
    current_time = 0
    frame = 0
    def getImgInfo(self):
        self.current_time += 1
        if self.current_time - self.animation_timer > self.animation_delay:
            self.frame += 1
            # Reset the walk counter if it exceeds the length of the charwalk list
            if self.frame >= len(self.fireImg):
                self.frame = 0
            # Update the animation timer
            self.animation_timer = self.current_time
        # return image info
    
        return (self.fireImg[self.frame], self.x, self.y)
    
    def getHitbox(self):
        return (self.x + 13, self.y + 25, self.width - 30, self.height - 40)
    
    
class waterObs(Model):
   # waterImg = [pygame.image.load("assets/water/water1.png"),pygame.image.load("assets/water/water2.png"),pygame.image.load("assets/water/water3.png"),pygame.image.load("assets/water/water1.png"),pygame.image.load("assets/water/water2.png"),pygame.image.load("assets/water/water1.png")]
    waterImg = [pygame.image.load("assets/water/water2.png"),pygame.image.load("assets/water/water3.png"),pygame.image.load("assets/water/water2.png"),pygame.image.load("assets/water/water3.png")]

    animation_timer = 0
    animation_delay = 10 # Animation delay 
    current_time = 0
    frame = 0
    def getImgInfo(self):
        self.current_time += 1
        if self.current_time - self.animation_timer > self.animation_delay:
            self.frame += 1
            # Reset the walk counter if it exceeds the length of the charwalk list
            if self.frame >= len(self.waterImg):
                self.frame = 0
            # Update the animation timer
            self.animation_timer = self.current_time
        # return image info
    
        return (self.waterImg[self.frame], self.x, self.y)
    
    def getHitbox(self):
        return (self.x + 80, self.y + 100, self.width  -50, self.height - 50)

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
    charwalk = [pygame.image.load("assets/charmander/walk1.png"), pygame.image.load("assets/charmander/walk2.png"), pygame.image.load("assets/charmander/walk3.png"), pygame.image.load("assets/charmander/walk4.png")]
    charjump = pygame.image.load("assets/charmander/jump.png")
    squirwalk = [pygame.image.load("assets/squirtle/walk1.png"), pygame.image.load("assets/squirtle/walk2.png"), pygame.image.load("assets/squirtle/walk3.png"), pygame.image.load("assets/squirtle/walk4.png")]
    squirjump = pygame.image.load("assets/squirtle/jump.png")
    bulbwalk = [pygame.image.load("assets/bulbasaur/walk1.png"), pygame.image.load("assets/bulbasaur/walk2.png"), pygame.image.load("assets/bulbasaur/walk3.png"), pygame.image.load("assets/bulbasaur/walk4.png")]
    bulbjump = pygame.image.load("assets/bulbasaur/jump.png")
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
            if self.curChar == 0:
                return (self.charjump, self.x, self.y)
            elif self.curChar == 1:
                return (self.squirjump, self.x, self.y)
            elif self.curChar == 2:
                return (self.bulbjump, self.x, self.y)
        
        if self.curChar == 0: 
            return (self.charwalk[self.walk], self.x, self.y)
        elif self.curChar == 1:
            return (self.squirwalk[self.walk], self.x, self.y)
        elif self.curChar == 2:
            return (self.bulbwalk[self.walk], self.x, self.y)
            
    
    #gets hitbox for character. A little smaller than what you see to allow for some on-the-edge gameplay
    def getHitbox(self):
        return (self.x + 13, self.y + 25, self.width - 30, self.height - 40)


