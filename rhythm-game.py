# Functions
from random import randrange
linesNo = 4
yOffset = 175
lineHeight = 2
lineOffset = 50

def drawLines():
    for i in range(linesNo):
        y = (yOffset-(lineHeight/2)) + (lineOffset * i)
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, y, 750, lineHeight))

playerHeight = 20
playerWidth = 4
playerOffset = 50

def drawPlayer(lineNumber):
    y = (yOffset-(playerHeight/2)) + (lineOffset * lineNumber)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect((playerOffset-(playerWidth/2)),y,playerWidth,playerHeight))

objects = [
]

colors = [
    (0,0,255),
    (0,255,0),
    (255,0,255),
    (255,255,0)
]

def updateObjects():
    if objects:
        for object in objects:
            object[0] = object[0]-3
            if object[0] <= playerOffset:
                if playerPosition == object[1]:
                    objects.remove(object)
            elif object[0] <= 0:
                print "game over"
            y = (yOffset-(playerHeight/2)) + (lineOffset * object[1])
            pygame.draw.rect(screen, colors[object[1]], pygame.Rect(object[0],y,playerHeight,playerHeight))
    else:
        print "no objects"
        objects.append([750,randrange(0, 4, 1)])

# The actual game
import pygame

pygame.init()
screen = pygame.display.set_mode((750,500)#, pygame.FULLSCREEN, 16
    )

playerPosition = 0
clock = pygame.time.Clock()
done = False

while not done:
    clock.tick(60)
    screen.fill((0,0,0))
    drawLines()
    drawPlayer(playerPosition)
    updateObjects()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerPosition = 0
            elif event.key == pygame.K_UP:
                playerPosition = 1
            elif event.key == pygame.K_RIGHT:
                playerPosition = 2
            elif event.key == pygame.K_DOWN:
                playerPosition = 3
        pygame.display.flip()

pygame.display.quit()
pygame.quit()
