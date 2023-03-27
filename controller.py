import pygame, sys, math, random
from model import Model, obstacle1
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1300, 675

#helper variables
bg = 0
tiles = 0
scroll = 0

class Controller:
    def __init__(self, v):
        self.view = v
        self.clock = pygame.time.Clock()
        self.obstacles = []
    
        self.trigger = pygame.USEREVENT + 2
        pygame.time.set_timer(self.trigger, random.randrange(2000, 3500))
    
    def startGame(self):
        #game quit
        #can only happen after view has been initalized I guess
        global bg, tiles
        bg = pygame.image.load("assets/background.png").convert()
        tiles = math.ceil(SCREEN_WIDTH / (bg.get_width())) + 1
        
        while True:
            for event in self.view.getEvents():
                if event.type == pygame.QUIT:
                    self.view.endGame()
                    sys.exit()
                if event.type == self.trigger:
                    self.obstacles.append(obstacle1(1350, 300, 300, 156))
            
            self.moveObstacles()
            
            self.updateBackground()
            for obs in self.obstacles:
                obsData = obs.getImgInfo()
                self.view.blitImg(obsData[0], obsData[1], obsData[2])
        
            self.view.update()
            self.clock.tick(60)
    
    def moveObstacles(self):
        obstacles_to_remove = []
        for obs in self.obstacles:
            obs.x -= 2
            if obs.x + obs.width < -400:
                obstacles_to_remove.append(obs)
        for obs in obstacles_to_remove:
            self.obstacles.remove(obs)
            
    def updateBackground(self):
        global scroll, tiles, bg
        for i in range(-1, tiles):
            w = bg.get_width()
            self.view.blitImg(bg, (i * w + scroll % w), 0)
        scroll -= 2
        if abs(scroll) > bg.get_width():
            scroll %= bg.get_width()