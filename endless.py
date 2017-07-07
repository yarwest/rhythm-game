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

def drawPlayer():
    y = (yOffset-(playerHeight/2)) + (lineOffset * playerPosition)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect((playerOffset-(playerWidth/2)),y,playerWidth,playerHeight))

objects = [
]

colors = [
    (0,0,255),
    (0,255,0),
    (255,0,255),
    (255,255,0)
]

timeThreshold = 5

def updateObjects():
    global deltaTime
    global score
    if objects:
        while deltaTime >= timeThreshold:
            for object in objects:
                object[0] -= 1
                if object[0] <= playerOffset:
                    if playerPosition == object[1]:
                        score += 1
                        objects.remove(object)
                if object[0] <= 0:
                    print "game over"
                    objects.remove(object)
            deltaTime -= timeThreshold
        for object in objects:
            y = (yOffset-(playerHeight/2)) + (lineOffset * object[1])
            pygame.draw.rect(screen, colors[object[1]], pygame.Rect(object[0],y,playerHeight,playerHeight))
    else:
        objects.extend((
            [750,randrange(0, linesNo, 1)],
            [850,randrange(0, linesNo, 1)],
            [950,randrange(0, linesNo, 1)],
            [1050,randrange(0, linesNo, 1)]
        ))

def drawScore():
    scoreText=font.render(str(score), 1,(255,0,0))
    screen.blit(scoreText, (350, 100))

# The actual game
import pygame

pygame.init()
screen = pygame.display.set_mode((750,500)#, pygame.FULLSCREEN, 16
    )

font=pygame.font.Font(None,30)
playerPosition = 0
deltaTime = 0
score = 0
clock = pygame.time.Clock()
done = False

while not done:
    deltaTime += clock.tick()
    screen.fill((0,0,0))
    drawLines()
    drawPlayer()
    updateObjects()
    drawScore()
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

pygame.display.quit()
pygame.quit()
