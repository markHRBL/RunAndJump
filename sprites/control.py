import pygame

class HelpControl(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(r"assets\images\control.png")
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width()-150

        self.draww = True

    def draw(self, surface):
        if self.draww == True:
            surface.blit(self.image, self.rect)