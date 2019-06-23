import pygame
from .endless import EndlessController
from .UI import UIController
from .UI import Button
from .UI import Text
class GameMaster:
    
    controls = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]
    
    def __init__(self):
        global done
        done = False

        self.screen = pygame.display.set_mode((750,500)#, pygame.FULLSCREEN, 16
            )
        
        pygame.font.init()
        self.font = pygame.font.Font(None,30)
        
        self.uiController = UIController(self.screen, self.font)
        self.eventWatcher = EventWatcher()
        self.eventWatcher.watch(self.uiController)

    @staticmethod
    def quitGame():
        global done
        print("bye bye")
        done = True

    def mainMenu(self):
        controller = MainMenuController(self)
        controller.init(self.font)

    def playEndless(self):
        controller = EndlessController(self.screen, self.font)
        controller.init()

    def options(self):
        controller = OptionsController(self)
        controller.init(self.font)
        print("options")

class EventWatcher:
    subscribers = []

    @staticmethod
    def subscribe(subscriber):
        EventWatcher.subscribers.append(subscriber)

    def watch(self, uiController):
        global done
        done = False
        while not done:
            uiController.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameMaster.quitGame()
                else:
                    for subscriber in self.subscribers:
                        subscriber.receiveEvent(event)
                pygame.display.flip()

class MainMenuController:
    buttons = [[30,30,"Endless Mode"],[30,100,"Options"],[30,170,"Exit to Desktop"]]
    
    def __init__(self, gameMaster):
        self.gameMaster = gameMaster

    def init(self, font):
        #pygame.mixer.music.load("audio/music/main-music.mp3")
        #pygame.mixer.music.play(-1)
        for button in self.buttons:
            UIController.registerDrawable(Button(button[0], button[1], button[2], (0,0,0), font))
        EventWatcher.subscribe(self)

    def receiveEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if event.pos[0] >= button[0] and event.pos[0] <= button[0] + 180 and event.pos[1] >= button[1] and event.pos[1] <= button[1] + 60:
                    #currentColor = 1 if currentColor==0 else 0
                    if button[2] == "Endless Mode":
                        self.gameMaster.playEndless()
                    elif button[2] == "Options":
                        self.gameMaster.options()
                    elif button[2] == "Exit to Desktop":
                        GameMaster.quitGame()


class OptionsController:
    def __init__(self, gameMaster):
        self.gameMaster = gameMaster

    def init(self, font):
        for i in range(4):
            buttonY = 30 + (70*i)
            UIController.registerDrawable(Text(30, buttonY + 20, "Button " + str(i + 1), (255,255,255), font))
            UIController.registerDrawable(Button(120, buttonY, str(self.gameMaster.controls[i]), (0,0,0), font))
        EventWatcher.subscribe(self)

    def receiveEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(4):
                buttonY = 30 + (70*i)
                if event.pos[0] >= 120 and event.pos[0] <= 120 + 180 and event.pos[1] >= buttonY and event.pos[1] <= buttonY + 60:
                    self.changeButton(i)

    def changeButton(self, index):
        print("changing button " + str(index))