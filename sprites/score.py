import pygame
import sys

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.points = 0

        self.font = pygame.font.Font(r'assets\\fonts\\Itim-Regular.ttf', 30)
        self.image = self.font.render("Score: %s" %(self.points), True, (57, 62, 70))
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.x = 49
        self.rect.y = 117

        self.die = False


    def get_score(self):
        score_get = self.points
        if score_get < 0 and self.die == True:
            score_get = 0
        return score_get
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def set_score(self, point):
        self.points+=point
        self.image = self.font.render("Score: %s" %(self.points), True, (57, 62, 70))


class Over(pygame.sprite.Sprite):
    def __init__(self, score):
        super().__init__()

        self.over_game = False

        self.image = pygame.image.load(r'assets\\images\\gameover.png')
        self.rect = self.image.get_rect()

        self.font = pygame.font.Font(r"assets\fonts\Itim-Regular.ttf", 30)
        self.image2 = self.font.render("Score: %s" %(score), True, (57, 62, 70))
        self.rect2 = self.image2.get_rect()

        self.rect2.x = 300
        self.rect2.y = 250

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image2, self.rect2)

    def over(self, function):
        clock = pygame.time.Clock()

        while True:
            clock.tick(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                function()