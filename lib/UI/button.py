import pygame
from .text import Text
class Button:
    buttonWidth = 180
    buttonHeight = 60
    color = (153, 0, 0)

    def __init__(self, posX, posY, text, color, font):
        self.rect = pygame.Rect(posX, posY, self.buttonWidth, self.buttonHeight)
        self.text = Text(posX + 15, posY + 20, text, color, font)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        self.text.draw(screen)
