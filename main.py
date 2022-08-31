from turtle import update
import pygame
from pygame.locals import *
from random import randint
from math import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STEP = 75

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TuxThinking')

pygame.font.init()
font = pygame.font.SysFont('Arial', 15)

level_settings = {
    'board': [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, -2, 0, 0, 0, 0, 0, 0]
        ],
    'steps': 0
}

guides = [
    ((0, 2), (2, 0), (0, -2), (-2, 0)),
    ((1,-2), (2, 1), (-1, 2), (-2, -1))
]

class enemy:
    def __init__(self, guide, position):
        self.guide = guide 
        self.position = position

    def get_step(self, level_step):
        step = self.guide[level_step if level_step <= len(self.guide) - 1 else level_step % 4]
        return step


def render_level(screen, level_settings):
    position_info = {
        'tux': None,
        'badguys': []
    }

    for i in range(0, 8):
        for j in range(0, 8):
            if level_settings['board'][j][i] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (i*STEP, j*STEP, STEP, STEP))
                position_info['tux'] = [i, j]
            elif level_settings['board'][j][i] == 2:
                pygame.draw.rect(screen, (255, 255, 0), (i*STEP, j*STEP, STEP, STEP))
            elif level_settings['board'][j][i] == -1:
                position_info['badguys'].append(enemy(guides[0], [j, i]))

    return position_info    


def update(info):
    global level_settings
    for enemy in info['badguys']:
        step = enemy.get_step(level_settings['steps'])
        level_settings['board'][enemy.position[1] + step[1]][enemy.position[0] + step[0]] = -1
        level_settings['board'][enemy.position[1]][enemy.position[0]] = 0     
    level_settings['steps'] += 1



clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    info = render_level(screen, level_settings)
    x = info['tux'][0]
    y = info['tux'][1]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            level_settings['board'][y][x-1] = 1
            level_settings['board'][y][x] = 0     
            update(info)
        elif key_input[pygame.K_UP]:
            level_settings['board'][y-1][x] = 1
            level_settings['board'][y][x] = 0 
            update(info)
        elif key_input[pygame.K_RIGHT]:
            level_settings['board'][y][x+1] = 1
            level_settings['board'][y][x] = 0
            update(info)
        elif key_input[pygame.K_DOWN]:
            level_settings['board'][y+1][x] = 1
            level_settings['board'][y][x] = 0
            update(info)


    pygame.display.flip()
    pygame.display.update()
