
import pygame
from random import randrange
class EndlessController:
    # Number of lines on the screen
    linesNo = 4
    # The start y-position of the lines
    yOffset = 175
    # The height of the lines
    lineHeight = 2
    # The (y-)space between the lines
    lineOffset = 50
    # Height of the player figure
    playerHeight = 20
    # Width of the player figure
    playerWidth = 4
    # The space between the player and the left side of the screen
    playerOffset = 50
    # The object colors
    colors = [
        (0,0,255),
        (0,255,0),
        (255,0,255),
        (255,255,0)
    ]
    # The time difference in milliseconds between every object move
    timeThreshold = 5
    clock = pygame.time.Clock()

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    # Function responsible for drawing all the lines on the designated locations
    def drawLines(self):
        for i in range(self.linesNo):
            y = (self.yOffset-(self.lineHeight/2)) + (self.lineOffset * i)
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0, y, 750, self.lineHeight))

    # Function for drawing the player in his spot
    def drawPlayer(self):
        y = (self.yOffset-(self.playerHeight/2)) + (self.lineOffset * self.playerPosition)
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect((self.playerOffset-(self.playerWidth/2)),y,self.playerWidth,self.playerHeight))

    # Function for updating the position and drawing the objects on the lines
    # Also responsible for adding new objects, tracking the score, and tracking the failure state
    def updateObjects(self):
        if self.objects:
            while self.deltaTime >= self.timeThreshold:
                for obj in self.objects:
                    obj[0] -= 1
                    if obj[0] <= self.playerOffset and obj[0] >= 30:
                        if self.playerPosition == obj[1]:
                            self.score += 1
                            self.objects.remove(obj)
                    if obj[0] <= 0:
                        print "game over"
                        self.objects.remove(obj)
                        self.done = True
                self.deltaTime -= self.timeThreshold
            for obj in self.objects:
                y = (self.yOffset-(self.playerHeight/2)) + (self.lineOffset * obj[1])
                pygame.draw.rect(self.screen, self.colors[obj[1]], pygame.Rect(obj[0],y,self.playerHeight,self.playerHeight))
        else:
            self.objects.extend((
                [750,randrange(0, self.linesNo, 1)],
                [850,randrange(0, self.linesNo, 1)],
                [950,randrange(0, self.linesNo, 1)],
                [1050,randrange(0, self.linesNo, 1)]
            ))

    # Function for drawing the score
    def drawScore(self):
        scoreText=self.font.render(str(self.score), 1,(255,0,0))
        self.screen.blit(scoreText, (350, 100))

    def updateScreen(self):
        # Add the time difference to the time difference variable
        self.deltaTime += self.clock.tick()
        # Reset the background and call all the drawing functions
        self.screen.fill((0,0,0))
        self.drawLines()
        self.drawPlayer()
        self.updateObjects()
        self.drawScore()
        # Update the display with everything that has been drawn
        pygame.display.flip()

    def play(self):
        # Storing the objects on the lines
        self.objects = []
        # A few variables for tracking the score, timedifference, score, etc.
        self.playerPosition = 0
        self.deltaTime = 0
        self.score = 0
        self.done = False
        while not self.done:
            self.updateScreen()
            # Handle every event that happens
            for event in pygame.event.get():
                # Finish the program when the game is being quit
                if event.type == pygame.QUIT:
                    self.done = True
                # Update the players position based on the keyboard input
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.playerPosition = 0
                    elif event.key == pygame.K_UP:
                        self.playerPosition = 1
                    elif event.key == pygame.K_RIGHT:
                        self.playerPosition = 2
                    elif event.key == pygame.K_DOWN:
                        self.playerPosition = 3
