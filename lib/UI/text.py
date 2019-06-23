import pygame
class Text:

    def __init__(self, posX, posY, text, color, font):
        self.rendered = font.render(text, 1, color)
        self.posX = posX
        self.posY = posY

    def draw(self, screen):
        screen.blit(self.rendered, (self.posX, self.posY))