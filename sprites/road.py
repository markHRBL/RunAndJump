import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load(r"assets\\images\\road.png")
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.x = 0
        self.rect.y = 360

    def draw(self, surface):
        surface.blit(self.image, self.rect)