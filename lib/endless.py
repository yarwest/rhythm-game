import pygame
from random import randrange
from . import gameMaster
from .UI import UIController
from .UI import Text
from .UI import Rect

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

    def __init__(self, font, gameMasterInstance):
        self.font = font
        self.gameMasterInstance = gameMasterInstance

    # Function responsible for drawing all the lines on the designated locations
    def drawLines(self):
        for i in range(self.linesNo):
            y = (self.yOffset-(self.lineHeight/2)) + (self.lineOffset * i)
            UIController.registerDrawable('game_lines', Rect(0, y, 750, self.lineHeight, (255,255,255)))

    # Function for drawing the player in his spot
    def updatePlayer(self):
        UIController.removeByLabel('game_player')
        y = (self.yOffset-(self.playerHeight/2)) + (self.lineOffset * self.playerPosition)
        UIController.registerDrawable('game_player', Rect(self.playerOffset-(self.playerWidth/2), y, self.playerWidth, self.playerHeight, (255,0,0)))

    # Function for updating the position
    # Also responsible for adding new objects, tracking the score, and tracking the failure state
    def updateObjects(self):
        if self.objects:
            while self.deltaTime >= self.timeThreshold:
                for i, obj in enumerate(self.objects):
                    obj[0] -= 1
                    if obj[0] <= self.playerOffset and obj[0] >= 30:
                        if self.playerPosition == obj[1]:
                            self.updateScore(1)
                            self.objects.remove(obj)
                    if obj[0] <= 0:
                        print("game over")
                        self.selfDestruct()
                        return
                self.deltaTime -= self.timeThreshold
            UIController.removeByLabel('game_object_0')
            UIController.removeByLabel('game_object_1')
            UIController.removeByLabel('game_object_2')
            UIController.removeByLabel('game_object_3')

            for i, obj in enumerate(self.objects):
                y = (self.yOffset-(self.playerHeight/2)) + (self.lineOffset * obj[1])
                UIController.registerDrawable('game_object_' + str(i), Rect(obj[0], y, self.playerHeight, self.playerHeight, self.colors[obj[1]]))
        else:
            self.objects.extend((
                [750,randrange(0, self.linesNo, 1)],
                [850,randrange(0, self.linesNo, 1)],
                [950,randrange(0, self.linesNo, 1)],
                [1050,randrange(0, self.linesNo, 1)]
            ))

    # Function for drawing the score
    def updateScore(self, difference):
        self.score += difference
        UIController.removeByLabel('game_current_score')
        UIController.registerDrawable('game_current_score', Text(350, 100, str(self.score), (255, 0, 0), self.font))

    def init(self):
        # Storing the objects on the lines
        self.objects = []
        # A few variables for tracking the score, timedifference, score, etc.
        self.playerPosition = 0
        self.deltaTime = 0
        self.score = 0

        self.drawLines()
        self.updatePlayer()
        self.updateScore(0)

        gameMaster.EventWatcher.subscribeTicks(self)
        gameMaster.EventWatcher.subscribeEvents(self)

    def receiveTick(self):
        self.deltaTime += self.clock.tick()
        self.updateObjects()

    def receiveEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerPosition = 0
                self.updatePlayer()
            elif event.key == pygame.K_UP:
                self.playerPosition = 1
                self.updatePlayer()
            elif event.key == pygame.K_RIGHT:
                self.playerPosition = 2
                self.updatePlayer()
            elif event.key == pygame.K_DOWN:
                self.playerPosition = 3
                self.updatePlayer()

    def selfDestruct(self):
        UIController.removeByLabel('game_current_score')
        UIController.removeByLabel('game_player')
        UIController.removeByLabel('game_lines')
        UIController.removeByLabel('game_object_0')
        UIController.removeByLabel('game_object_1')
        UIController.removeByLabel('game_object_2')
        UIController.removeByLabel('game_object_3')

        gameMaster.EventWatcher.unsubscribeEvents(self)
        gameMaster.EventWatcher.unsubscribeTicks(self)

        self.gameMasterInstance.mainMenu()