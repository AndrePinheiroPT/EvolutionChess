import pygame
from pygame.locals import *
from random import randint
from math import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STEP = 75

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('EvolutionChess')

pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
time = 0

interactions = 0
tux_position = [0,0]
target = [6, 3]
board = []

test = [(0, 2), (2, 0), (0, -2), (-2, 0)]

class enemy:
    def __init__(self, init_pos, movements):
        self.position = init_pos
        self.guide = movements
        self.guide_step = 0

    def move_enemy(self, interations):
        if self.guide_step >= len(self.guide):
            self.guide_step = interactions % len(self.guide) - 1
        for i in range(0, 2):
            self.position[i] += self.guide[self.guide_step][i]
        self.guide_step += 1    

    def draw_enemy(self, screen, color):
        pygame.draw.rect(screen, color, (self.position[0]*STEP, self.position[1]*STEP, STEP, STEP))

badguy = enemy([5, 2], test)

def update():
    global interactions, badguy
    interactions += 1
    badguy.move_enemy(interactions)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            tux_position[0] -= 1 
            update()
        if key_input[pygame.K_UP]:
            tux_position[1] -= 1 
            update()
        if key_input[pygame.K_RIGHT]:
            tux_position[0] += 1 
            update()
        if key_input[pygame.K_DOWN]:
            tux_position[1] += 1 
            update()


    pygame.draw.rect(screen, (0, 0, 255), (tux_position[0]*STEP, tux_position[1]*STEP, STEP, STEP))
    pygame.draw.rect(screen, (255, 255, 0), (target[0]*STEP, target[1]*STEP, STEP, STEP))
    badguy.draw_enemy(screen, (0, 0, 100))


    pygame.display.flip()
    pygame.display.update()
