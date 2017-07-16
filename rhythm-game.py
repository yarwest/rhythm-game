import pygame
from endless import EndlessController

# Initialize pygame and open a display
pygame.init()
screen = pygame.display.set_mode((750,500)#, pygame.FULLSCREEN, 16
    )

# A few variables to Initialize the menu
font=pygame.font.Font(None,30)
color = (153, 0, 0)
buttons = [[30,30,"Endless Mode"],[30,100,"Options"],[30,170,"Exit to Desktop"]]
buttonWidth = 180
buttonHeight = 60
done = False
controller = EndlessController(screen, font)

def initMainMenuButtons():
    screen.fill((0,0,0))
    for button in buttons:
        pygame.draw.rect(screen, color, pygame.Rect(button[0], button[1], buttonWidth, buttonHeight))
        buttonText=font.render(button[2], 1,(0,0,0))
        screen.blit(buttonText, (button[0]+15, button[1]+20))

def quitGame():
    global done
    print "bye bye"
    done = True

#pygame.mixer.music.load("audio/music/main-music.mp3")
#pygame.mixer.music.play(-1)

while not done:
    initMainMenuButtons()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if event.pos[0] >= button[0] and event.pos[0] <= button[0]+buttonWidth and event.pos[1] >= button[1] and event.pos[1] <= button[1]+buttonHeight:
                    #currentColor = 1 if currentColor==0 else 0
                    if button[2] == "Endless Mode":
                        controller.play()
                    elif button[2] == "Options":
                        print "options"
                    elif button[2] == "Exit to Desktop":
                        quitGame()
        pygame.display.flip()
