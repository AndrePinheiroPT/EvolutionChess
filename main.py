import pygame
from pygame.locals import *
from random import randint
from math import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STEP = 25

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('EvolutionChess')

pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
time = 0

list_colors = [(randint(0,255), randint(0,255), randint(0, 255)) for i in range(0, 20)]
population = [
    [0, 1, 0, 1, 1, 0] # <- Genome
]

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.draw.rect(screen, list_colors[1], (5*STEP, 5*STEP, STEP, STEP))

    pygame.display.flip()
    pygame.display.update()
