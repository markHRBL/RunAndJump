import pygame
import random

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(r"assets\\images\\player.png")
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width()/2-70
        self.rect.y = 300
        self.jumping = False
        self.height = 30
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self):
        surface = pygame.display.get_surface()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x >= 0:
            self.rect.x -= 10
        elif keys[pygame.K_d] and self.rect.x <= surface.get_width()-80:
            self.rect.x += 10
        if keys[pygame.K_SPACE]:
            self.jumping = True

        if self.jumping:
            self.jump()

    def jump(self):
        self.rect.y -= self.height
        self.height -= 3
        if self.height < -30:
            self.height = 30
            self.jumping = False