import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random
from os import listdir


pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 1200, 800

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

main_surface = pygame.display.set_mode(screen)

#player = pygame.Surface((20, 20))
#player.fill(WHITE)
IMG_PATH = 'images/goose'
PLAYER_IMGS = [pygame.image.load(IMG_PATH + '/' + file).convert_alpha() for file in listdir(IMG_PATH)]
player = PLAYER_IMGS[0]
player_rect = player.get_rect()
player_speed = 5

ENEMY_IMG = pygame.image.load('images/enemy.png').convert_alpha()
BONUS_IMG = pygame.image.load('images/bonus.png').convert_alpha()

def create_enemy():
    #enemy = pygame.Surface((20, 20))
    # enemy.fill(RED)
    enemy = ENEMY_IMG
    enemy_rect = pygame.Rect(width, random.randint(enemy.get_height(), height - enemy.get_height()), *enemy.get_size())
    enemy_speed = random.randint(4, 6)
    return [enemy, enemy_rect, enemy_speed]

def create_bonus():
    #bonus = pygame.Surface((20, 20))
    #2bonus.fill(GREEN)
    bonus = BONUS_IMG
    bonus_rect = pygame.Rect(random.randint(bonus.get_width(), width - bonus.get_width()), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
enemies = []

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)
bonuses = []

CHANGE_IMGS = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMGS, 125)
player_idx = 0

font = pygame.font.SysFont('Verdana', 20)
score = 0

bg = pygame.transform.scale(pygame.image.load('images/background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMGS:
            player_idx += 1
            if player_idx >= len(PLAYER_IMGS):
                player_idx = 0
            player = PLAYER_IMGS[player_idx]

    #main_surface.fill(BLACK)

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()

    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(player, player_rect)
    main_surface.blit(font.render(str(score), True, GREEN), (width - 30, 0))

    # process hero movement
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_DOWN] and not player_rect.bottom + player_speed > height:
        player_rect = player_rect.move(0, player_speed)
    if pressed_keys[K_UP] and not player_rect.top < 0:
        player_rect = player_rect.move(0, -player_speed)
    if pressed_keys[K_RIGHT] and not player_rect.right + player_speed > width:
        player_rect = player_rect.move(player_speed, 0)
    if pressed_keys[K_LEFT] and not player_rect.left - player_speed < 0:
        player_rect = player_rect.move(-player_speed, 0)

    # process enemies
    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].right < 0:
            enemies.pop(enemies.index(enemy))

        elif player_rect.colliderect(enemy[1]):
            is_working = False

    # process bonuses
    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].top > height:
            bonuses.pop(bonuses.index(bonus))
        else:
            if player_rect.colliderect(bonus[1]):
                bonuses.pop(bonuses.index(bonus))
                score = score + 1


    pygame.display.flip()