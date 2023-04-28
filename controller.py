import pygame, sys, math, random, time
from model import Model, obstacle1, obstacle2, character, waterObs, fireObs, grassObs, snorObs, hPack
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1300, 600
FLOOR = 490
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
        self.triggerDelay = 2500
        self.triggerDelay2 = 2600
        self.trigger = pygame.USEREVENT + 2
        pygame.time.set_timer(self.trigger, random.randrange(self.triggerDelay, self.triggerDelay2))
        self.clockspeed = 60
        self.score = 0
        
    def startGame(self):
        #game quit
        global bg, tiles, scroll
        bg = pygame.image.load("assets/background7.png").convert()
        startImg = pygame.image.load("assets/loading/start.jpg")        
        tiles = math.ceil(SCREEN_WIDTH / (bg.get_width())) + 1
        jumpSound = pygame.mixer.Sound("assets/jump.mp3")
        
        #reads and stores current highscore
        highscore = 0
        with open('highscore.txt', 'r') as f:
            highscore = f.read()
        player = character(500, 410, 86, 100)
        
        font = pygame.font.SysFont("CourierNew", 72)
        txtsurf = font.render("Highscore: " + str(highscore), True, (0,0,0))
        font2 = pygame.font.SysFont("CourierNew", 40)
        txtsurf2 = 0
        
        
        input_received = False
        
        #start loading screen
        while not input_received:
            self.view.blitImg(startImg, 0, 0)
            self.view.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    input_received = True
                elif event.type == pygame.KEYDOWN:
                    input_received = True
        #game start       
        while True:
            
            for event in self.view.getEvents():
                if event.type == pygame.QUIT:
                    self.view.endGame()
                    sys.exit()
                                
                #generates new obstacles
                if event.type == self.trigger:
                    #chooses random obstacle to create
                    rand = random.randint(1,4)
                    self.score += 1
                    if rand == 1:
                        self.obstacles.append(snorObs(1350, FLOOR-52, 100, 52))
                    elif(rand == 2):
                        self.obstacles.append(fireObs(1350, FLOOR-280, 94, 300))
                    elif(rand == 3):
                        self.obstacles.append(waterObs(1350, FLOOR-350, 94, 300))
                    elif(rand == 4):
                        self.obstacles.append(grassObs(1350, FLOOR-251, 94, 300))
                    if self.clockspeed > 170:
                        self.score += 1
                        rand = random.randint(1,4)
                        buf = 450
                        if rand == 1:
                            self.obstacles.append(snorObs(1350 + buf, FLOOR-52, 100, 52))
                        elif(rand == 2):
                            self.obstacles.append(fireObs(1350+ buf, FLOOR-280, 94, 300))
                        elif(rand == 3):
                            self.obstacles.append(waterObs(1350 +buf, FLOOR-350, 94, 300))
                        elif(rand == 4):
                            self.obstacles.append(grassObs(1350 +buf, FLOOR-251, 94, 300))
            
            #starts to spawn health orbs if needed
            if player.health < 2.5:
                rand = random.randint(1, 50)
                if rand == 5:
                    if self.obstacles:
                        x = self.obstacles[len(self.obstacles) -1].x
                        if x + 220 > 1350:
                            y = random.randint(200, 400)
                            t = hPack(x + 220, y, 40, 40)
                            rand = random.randint(0,2)
                            t.pack = rand
                            self.obstacles.append(t)
                            for i in range(len(self.obstacles)):
                                if (i < len(self.obstacles) - 1) and type(self.obstacles[i]) is hPack:
                                    self.obstacles.remove(t)
            
            #loop for end screen                             
            if player.health <= 0:             
                player.jump = True
                self.movePlayer(player)
                pData = player.getImgInfo()
                self.updateBackground()
                for i in range(-1, tiles):
                    w = bg.get_width()
                    self.view.blitImg(bg, (i * w + scroll % w), 0)
                self.view.blitImg(pData[0], pData[1], pData[2])
                self.view.blitImg(txtsurf, 320, 100)
                self.view.blitImg(txtsurf2, 450, 200)
                self.view.update()
                self.clock.tick(60)
                continue
        
            self.moveObstacles()
            self.updateBackground()

            keys = self.view.getPressed()
            if keys[pygame.K_SPACE]:
                player.jump = True
                if player.y > 409:
                    pygame.mixer.Sound.play(jumpSound)
                
            
            mouse = self.view.getMousePressed()
            if mouse:
                if mouse[0]:
                    self.cycleChar(player)
            
            if(player.jump): 
                self.movePlayer(player)
            #print(player.y)
            playerHitbox = pygame.Rect(player.getHitbox())
            #blits all obstacles
            
            #dictates damage taken and draws obstacles
            for obs in self.obstacles:
                obsData = obs.getImgInfo()
                self.view.blitImg(obsData[0], obsData[1], obsData[2])
                #collison detection
                if pygame.Rect.colliderect(playerHitbox, pygame.Rect(obs.getHitbox())):
                    if player.curChar == 0 and (type(obs) is fireObs):
                        player.health -= 0.5
                    elif player.curChar == 0 and (type(obs) is waterObs):
                        player.health -= 1
                    elif player.curChar == 1 and (type(obs) is waterObs):
                        player.health -= 0.5
                    elif player.curChar == 1 and (type(obs) is grassObs):
                        player.health -= 1
                    elif player.curChar == 2 and (type(obs) is grassObs):
                        player.health -= 0.5
                    elif player.curChar == 2 and (type(obs) is fireObs):
                        player.health -= 1
                    elif type(obs) is snorObs:
                        player.health -= 1
                    elif type(obs) is hPack:
                        if obs.pack == player.curChar:
                            player.health += .5
                            self.obstacles.remove(obs)
                    if type(obs) is not hPack:
                        self.obstacles.remove(obs)
                    #print("GAME OVER DWEEB XDDD")
                   # pygame.time.delay(200)
                    
            self.drawHealth(player)
            
            #blits player
            pData = player.getImgInfo()
            self.view.blitImg(pData[0], pData[1], pData[2])
            self.updateClock()
            self.view.update()
            self.clock.tick(self.clockspeed)
            #game end 
            if player.health <= 0:
                if(self.score > float(highscore)):
                    with open('highscore.txt', 'w') as f:
                        f.write(str(self.score))
                    txtsurf = font.render("Highscore: " + str(self.score), True, (0,0,0))
                txtsurf2 = font2.render("Your Score: " + str(self.score), True, (0,0,0))


            
    #updates clock speed to make game faster
    def updateClock(self):
        if self.clockspeed > 100 and self.triggerDelay > 0:
            self.triggerDelay -= 10
            self.triggerDelay2 -= 10.8
        if self.clockspeed < 180:
            self.clockspeed += .05
        
    #draws hearts to represent health
    def drawHealth(self, player):
        packs = player.getHealth()
        x = 20
        y = 30
        for p in packs:
            self.view.blitImg(p, x, y)
            x += 100
    
    #cycles character
    def cycleChar(self, player):
        currentTime = time.time()
        if currentTime - self.lastCharChangeTime >= 0.2:
            player.curChar = (player.curChar + 1) % 3
            self.lastCharChangeTime = currentTime
    
    #for player controlled movements
    def movePlayer(self, player):

        if player.y < 610:
            player.y -= player.velocity
        
        player.velocity -= .2
        if player.velocity < -10:
            player.jump = False
            if player.health > 0:
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