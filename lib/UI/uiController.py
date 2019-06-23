import pygame
class UIController:
    drawables = {}
    
    def __init__(self, screen, font):
        # TODO: later make own screen and font
        UIController.screen = screen
        UIController.font = font


    @staticmethod
    def registerDrawable(label, drawable):
        if(label not in UIController.drawables):
            UIController.drawables[label] = []
        UIController.drawables[label].append(drawable)

    @staticmethod
    def removeByLabel(label):
        del UIController.drawables[label]

    @staticmethod
    def draw():
        UIController.screen.fill((0,0,0))
        for label, drawables in UIController.drawables.items():
            for drawable in drawables:
                drawable.draw(UIController.screen)