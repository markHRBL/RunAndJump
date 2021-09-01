import pygame
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(r"assets\\images\\enemyimg.png")
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.x = -random.randint(600, 1500)-surface.get_width()
        self.rect.y = 320
        self.direction = 1
        self.cooldown = random.randint(600, 1500)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        surface = pygame.display.get_surface()
        self.rect.x += 6 * self.direction
        if self.rect.x > self.cooldown:
            self.direction = -1
            self.cooldown = random.randint(600, 1500)
        elif self.rect.x < (-1)*self.cooldown-10:
            self.direction = 1
            self.cooldown = random.randint(600, 1500)
