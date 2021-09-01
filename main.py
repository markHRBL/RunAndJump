import pygame
import sys
from sprites.road import Road
from sprites.player import Player
from sprites.ball import Ball
from sprites.score import Score
from sprites.score import Over
from sprites.enemy import Enemy
from sprites.ice import Ice
from sprites.control import HelpControl
from sprites.menu import MainMenu, PlayButton

pygame.init()

WIDTH = 700
HEIGHT = 400
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Run&Jump")

def start_menu():
    clock = pygame.time.Clock()
    menu_bg = MainMenu()
    play_btn = PlayButton()


    menu = True
    while menu:

        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if play_btn.rect.collidepoint(pygame.mouse.get_pos()):
                    menu = False
                    restart()

        menu_bg.draw(screen)
        play_btn.draw(screen)
        pygame.display.update()

def restart():
    clock = pygame.time.Clock()

    road = Road()
    player = Player()
    balls = pygame.sprite.Group()
    score = Score()
    enemy = Enemy()
    ice = Ice()
    help_control = HelpControl()

    running = True
    while running:
        clock.tick(FPS)
        player.update()
        balls.update(screen)
        if len(balls) < 1:
            ball = Ball()
            balls.add(ball)
        enemy.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.sprite.spritecollide(player, balls, True):
            score.set_score(1)
            if score.get_score() >= 3:
                help_control.draww = False
        if pygame.sprite.spritecollide(road, balls, True) or pygame.sprite.spritecollide(enemy, balls, True):
            score.set_score(-2)
            ball.kill()
            if score.get_score() < 0:
                ball.kill()

                score.die = True
                over = Over(score.get_score())
                over.draw(screen)
                pygame.display.update()
                over.over(restart)
        if pygame.sprite.collide_mask(enemy, player):
            if ice.get_count_ice() > 1:
                ice.set_count_ice(-1)
                if enemy.direction == -1:
                    enemy.rect.x -= -65
                    player.jumping = True
                    player.rect.x -= 65
                    enemy.direction = 1
                else:
                    enemy.rect.x += -65
                    player.jumping = True
                    player.rect.x += 65
                    enemy.direction = -1
            else:
                over = Over(score.get_score())
                over.draw(screen)
                pygame.display.update()
                over.over(restart)

        screen.fill((255, 255, 255))
        road.draw(screen)
        player.draw(screen)
        balls.draw(screen)
        score.draw(screen)
        enemy.draw(screen)
        ice.draw(screen)
        help_control.draw(screen)
        pygame.display.update()

start_menu()