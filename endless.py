## Functions ##
from random import randrange

# Number of lines on the screen
linesNo = 4
# The start y-position of the lines
yOffset = 175
# The height of the lines
lineHeight = 2
# The (y-)space between the lines
lineOffset = 50

# Function responsible for drawing all the lines on the designated locations
def drawLines():
    for i in range(linesNo):
        y = (yOffset-(lineHeight/2)) + (lineOffset * i)
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, y, 750, lineHeight))

# Height of the player figure
playerHeight = 20
# Width of the player figure
playerWidth = 4
# The space between the player and the left side of the screen
playerOffset = 50

# Function for drawing the player in his spot
def drawPlayer():
    y = (yOffset-(playerHeight/2)) + (lineOffset * playerPosition)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect((playerOffset-(playerWidth/2)),y,playerWidth,playerHeight))

# Storing the objects on the lines
objects = []
# The object colors
colors = [
    (0,0,255),
    (0,255,0),
    (255,0,255),
    (255,255,0)
]
# The time difference in milliseconds between every object move
timeThreshold = 5

# Function for updating the position and drawing the objects on the lines
# Also responsible for adding new objects, tracking the score, and tracking the failure state
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

# Function for drawing the score
def drawScore():
    scoreText=font.render(str(score), 1,(255,0,0))
    screen.blit(scoreText, (350, 100))


## The actual game ##
import pygame

# Initialize pygame and open a display
pygame.init()
screen = pygame.display.set_mode((750,500)#, pygame.FULLSCREEN, 16
    )

# A few variables for tracking the score, timedifference, score, etc.
font=pygame.font.Font(None,30)
playerPosition = 0
deltaTime = 0
score = 0
clock = pygame.time.Clock()
done = False

while not done:
    # Add the time difference to the time difference variable
    deltaTime += clock.tick()
    # Reset the background and call all the drawing functions
    screen.fill((0,0,0))
    drawLines()
    drawPlayer()
    updateObjects()
    drawScore()
    # Update the display with everything that has been drawn
    pygame.display.flip()
    # Handle every event that happens
    for event in pygame.event.get():
        # Finish the program when the game is being quit
        if event.type == pygame.QUIT:
            done = True
        # Update the players position based on the keyboard input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerPosition = 0
            elif event.key == pygame.K_UP:
                playerPosition = 1
            elif event.key == pygame.K_RIGHT:
                playerPosition = 2
            elif event.key == pygame.K_DOWN:
                playerPosition = 3
