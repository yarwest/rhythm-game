import pygame
class UIController:
    drawables = []
    
    def __init__(self, screen, font):
        # TODO: later make own screen and font
        self.screen = screen
        self.font = font


    @staticmethod
    def registerDrawable(drawable):
        UIController.drawables.append(drawable)

    def draw(self):
        self.screen.fill((0,0,0))
        for drawable in self.drawables:
            drawable.draw(self.screen)