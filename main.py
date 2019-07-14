import pygame
import math

pygame.init()
SRD = [800, 600]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
screen = pygame.display.set_mode(SRD)
done = False
pygame.display.set_caption("Fun with Discrete Fourier Transform")
clock = pygame.time.Clock()
time = 0
while(not done):
    clock.tick(60)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    screen.fill([0, 0, 0])
    center_x = 50
    center_y  = 300
    center = [center_x, center_y]
    ratio = 50
    pygame.draw.circle(screen, WHITE, center, ratio, 1)
    x = center_x + ratio * math.cos(time)
    y = center_y + ratio * math.sin(time)
    pygame.draw.line(screen, WHITE, center, [x, y])
    time += 0.1
    pygame.display.flip()
pygame.quit()

