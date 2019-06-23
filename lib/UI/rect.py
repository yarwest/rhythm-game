import pygame
class Rect:

    def __init__(self, posX, posY, width, height, color):
        self.rect = pygame.Rect(posX, posY, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)