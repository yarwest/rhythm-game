# Functions

def drawLines():
    for i in range(linesNo):
        y = 175 + (50 * i)
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, y, 750, 2))

def drawPlayer(lineNumber):
    y = 174 + (50 * lineNumber)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(23,y,4,4))

# The actual game
import pygame

pygame.init()
screen = pygame.display.set_mode((750,500)#, pygame.FULLSCREEN, 16
    )

linesNo = 4
playerPosition = 0
done = False

while not done:
    screen.fill((0,0,0))
    drawLines()
    drawPlayer(playerPosition)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()

pygame.display.quit()
pygame.quit()
