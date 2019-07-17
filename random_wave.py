import pygame
import math
import random
from fourier import *


pygame.init()
SRD = [800, 600]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
screen = pygame.display.set_mode(SRD)
done = False
pygame.display.set_caption("Fun with Discrete Fourier Transform")
clock = pygame.time.Clock()
signal = []
value = 50
for i in range(300):
    value += random.randint(-10, 10) 
    signal.append(value)
    
fouri = fourier(signal)
dft = fouri.get_transform()
time = 0
radius = 200
center_x = radius
center_y  = 300
center = [center_x, center_y]
begin = 2 * radius + 10
wave = [[begin, center_y]]
tick = 2 * math.pi / len(dft)
k = len(dft)
pause = False
while(not done):
    clock.tick(60)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if(not pause):
                    pause = True
                else:
                    pause = False
            if event.key == pygame.K_DOWN:
                if(k > 0 ):
                    k -=1
            if event.key == pygame.K_UP:
                if(k < len(dft)):
                    k += 1
            if event.key == pygame.K_LEFT:
                if(tick > 0.005):
                    tick -= 0.005
            if event.key == pygame.K_RIGHT:
                if(tick < 0.1):
                    tick += 0.005
            if event.key == pygame.K_c:
                    wave = [wave[0]]

    screen.fill([0, 0, 0])
    if(not pause):
        for w in wave:
            w[0] += 1
        
    x = center_x
    y = center_y
    for i in range(1, len(dft)):
        freq = dft[i].get('freq')
        radius = dft[i].get('amp')
        phase = dft[i].get('phase')
        if(radius >= 1):
            pygame.draw.circle(screen, WHITE, [int(x), int(y)], int(radius), 1)
        else:
            pygame.draw.circle(screen, WHITE, [int(x), int(y)], 1, 1)
        temp_x = x
        temp_y = y
        x = x + radius * math.cos(freq * time + phase)
        y = y + radius * math.sin(freq * time + phase)
        pygame.draw.line(screen, WHITE, [temp_x, temp_y], [x, y])
        pygame.draw.circle(screen, WHITE, [int(x), int(y)], 0, 0)
                    
    if(not pause):
        wave.insert(0, [begin, y])
        
        if(len(wave) > screen.get_width() - begin):
            wave.pop()
    for i in range(1, len(wave)):
        pygame.draw.line(screen, WHITE, wave[i - 1], wave[i])
    pygame.draw.line(screen, WHITE, [int(x), int(y)], wave[0])
    if(not pause):
        time -= tick
    pygame.display.flip()
pygame.quit()

