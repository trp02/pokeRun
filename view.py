import pygame, sys
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 600

class View:

    #initializes board
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        pygame.display.set_caption("Side scroller")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        
    #mostly just drawing functions
    #
    def blitImg(self, img, xCord, yCord):
        self.surface.blit(img, (xCord, yCord))
    
    def backgroundFill(self, color):
        self.surface.fill(color)

    def drawRect(self, color, rect):
        pygame.draw.rect(self.surface, color, rect, 2)
        
    def drawCirc(self, color, cords):
        pygame.draw.circle(self.surface, color, (cords[0], cords[1]), cords[2])
        
    #send events to controller
    def getEvents(self):
        return pygame.event.get()
    #button pressed to controller
    def getPressed(self):
        return pygame.key.get_pressed()
    
    def getMousePressed(self):
        return pygame.mouse.get_pressed()
    
    def update (self):
        pygame.display.update()
        
    def endGame(self):
        pygame.quit
    