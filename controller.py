import pygame, sys, math, random, time
from model import Model, obstacle1, obstacle2, character, waterObs, fireObs, grassObs
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1300, 675
FLOOR = 510
CHARFLOOR = 424
#helper variables
bg = 0
tiles = 0
scroll = 0

class Controller:
    def __init__(self, v):
        self.view = v
        self.clock = pygame.time.Clock()
        self.obstacles = []
        self.lastCharChangeTime = time.time()

        self.trigger = pygame.USEREVENT + 2
        pygame.time.set_timer(self.trigger, random.randrange(2000, 3500))
        
    def startGame(self):
        #game quit
        #can only happen after view has been initalized I guess
        global bg, tiles
        bg = pygame.image.load("assets/background.png").convert()
        tiles = math.ceil(SCREEN_WIDTH / (bg.get_width())) + 1
        
        player = character(500, 423, 86, 100)
        
        while True:
            for event in self.view.getEvents():
                if event.type == pygame.QUIT:
                    self.view.endGame()
                    sys.exit()
                    
                #generates new obstacle
                if event.type == self.trigger:
                    #chooses random obstacle to create
                    rand = random.randint(1,4)
                    if rand == 1:
                        self.obstacles.append(obstacle1(1350, FLOOR-52, 100, 52))
                    elif(rand == 2):
                        self.obstacles.append(fireObs(1350, FLOOR-280, 94, 300))
                    elif(rand == 3):
                        self.obstacles.append(waterObs(1350, FLOOR-350, 94, 300))
                    elif(rand == 4):
                        self.obstacles.append(grassObs(1350, FLOOR-240, 94, 300))

            
            self.moveObstacles()
            self.updateBackground()
            
            keys = self.view.getPressed()
            if keys[pygame.K_SPACE]:
                player.jump = True
            
            mouse = self.view.getMousePressed()
            if mouse:
                if mouse[0]:
                    self.cycleChar(player)
            
            if(player.jump): 
                self.movePlayer(player)
            #print(player.y)
            playerHitbox = pygame.Rect(player.getHitbox())
            #blits all obstacles
            for obs in self.obstacles:
                obsData = obs.getImgInfo()
                self.view.blitImg(obsData[0], obsData[1], obsData[2])
                self.view.drawRect((255,0,0), obs.getHitbox())
                if pygame.Rect.colliderect(playerHitbox, pygame.Rect(obs.getHitbox())):
                    pass 
                    #print("GAME OVER DWEEB XDDD")
                   # pygame.time.delay(200)
                    
        
            #blits player
            pData = player.getImgInfo()
            self.view.blitImg(pData[0], pData[1], pData[2])
          #  self.view.drawRect((255,0,0), player.getHitbox())
                
            self.view.update()
            self.clock.tick(60)
    
    
    
    def cycleChar(self, player):
        currentTime = time.time()
        if currentTime - self.lastCharChangeTime >= 0.2:
            player.curChar = (player.curChar + 1) % 3
            self.lastCharChangeTime = currentTime
    
    #for player controlled movements
    def movePlayer(self, player):

        player.y -= player.velocity
        player.velocity -= .2
            
        if player.velocity < -10:
            player.jump = False
            player.velocity = 10
        
    def moveObstacles(self):
        #keeps obstacles moving along with the background and removes once they go off screen
        obstacles_to_remove = []
        for obs in self.obstacles:
            obs.x -= 2
            if obs.x + obs.width < -300:
                obstacles_to_remove.append(obs)
        for obs in obstacles_to_remove:
            self.obstacles.remove(obs)
            
    def updateBackground(self):
        #updates background image 
        global scroll, tiles, bg
        for i in range(-1, tiles):
            w = bg.get_width()
            self.view.blitImg(bg, (i * w + scroll % w), 0)
        scroll -= 2
        if abs(scroll) > bg.get_width():
            scroll %= bg.get_width()