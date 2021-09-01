import pygame

class Ice(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.threeice = pygame.image.load(r"assets\images\threeice.png")
        self.twooice = pygame.image.load(r"assets\images\twooice.png")
        self.oneice = pygame.image.load(r"assets\images\oneice.png")
        self.zeroice = pygame.image.load(r"assets\images\zeroice.png")

        self.rect1 = self.threeice.get_rect()
        self.rect2 = self.twooice.get_rect()
        self.rect3 = self.oneice.get_rect()
        self.rect4 = self.zeroice.get_rect()

        self.count = 3

        self.rect1.x = 29
        self.rect1.y = 10

        self.rect2.x = 29
        self.rect2.y = 10

        self.rect3.x = 29
        self.rect3.y = 10

        self.rect4.x = 29
        self.rect4.y = 10

    def draw(self, surface):
        if self.count == 3:
            surface.blit(self.threeice, self.rect1)
        elif self.count == 2:
            surface.blit(self.twooice, self.rect2)
        elif self.count == 1:
            surface.blit(self.oneice, self.rect3)
        elif self.count == 0:
            surface.blit(self.zeroice, self.rect4)

    def update(self, surface):
        pass

    def get_count_ice(self):
        return self.count

    def set_count_ice(self, points):
        self.count+=points
