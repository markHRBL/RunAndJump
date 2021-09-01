import pygame
import random
import time

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(r'assets\\images\\ball.png')
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()

        Xself = random.randint(0, surface.get_width()-50)
        self.rect.x = Xself
        self.rect.y = 0
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, surface):
        self.rect.y += 5
