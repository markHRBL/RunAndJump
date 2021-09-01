import pygame

class MainMenu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(r"assets\images\menubackground.png")
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class PlayButton(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(r"assets\images\playbutton.png")
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.y = surface.get_height()/2
        self.rect.x = surface.get_width()/2-140

    def draw(self, surface):
        surface.blit(self.image, self.rect)