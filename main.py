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
center_x = 50
center_y  = 300
center = [center_x, center_y]
ratio = 50
begin = 300
wave = [[begin, center_y]]
tick = 0.1
int n = 2
while(not done):
    clock.tick(60)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    screen.fill([0, 0, 0])  
    for w in wave:
        w[0] += 1
    for i in range(n):
        pygame.draw.circle(screen, WHITE, center, ratio, 1)
        x = center_x + ratio * math.cos(time)
        y = center_y + ratio * math.sin(time)
        pygame.draw.circle(screen, WHITE, [int(x), int(y)], 5, 0)
    wave.insert(0, [begin, y])
    pygame.draw.line(screen, WHITE, center, [x, y])
    if(len(wave) > screen.get_width() - begin):
        wave.pop()
    for i in range(1, len(wave)):
        pygame.draw.line(screen, WHITE, wave[i - 1], wave[i])
    pygame.draw.line(screen, WHITE, [int(x), int(y)], wave[0])
    time += tick
    pygame.display.flip()
pygame.quit()

