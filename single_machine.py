import pygame
import math
import random
from fourier2d import *
from complex_number import *

pygame.init()
SRD = [800, 600]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
PURPLE = [148,0,211]
screen = pygame.display.set_mode(SRD)
done = False
pygame.display.set_caption("Fun with Discrete Fourier Transform")
clock = pygame.time.Clock()
signal = []
f_x = open('x.txt', 'r')
f_y = open('y', 'r')
value = 50
value2 = 50
for i in range(300):
    value += random.randint(-10, 10) 
    value2 += random.randint(-10, 10)
 

signal_x = []
signal_y = []
for line in f_x:
    aux = f_x.readline()
    
    signal_x.append(float(aux))
for line in f_y:
    aux = f_y.readline()
    signal_y.append(float(aux))
signal = []
for i in range(len(signal_x)):
    signal.append(complex_number(signal_x[i] + 100, signal_y[i] + 100))
print(signal)
f_x.close()
f_y.close()

fouri = fourier2d(signal)
dft = fouri.get_transform()
time = 0
radius = 200
center_x = 400
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
            if event.key == pygame.K_c:
                    wave = [wave[0]]

    screen.fill([0, 0, 0])

        
    x = center_x
    y = center_y
    for i in range(1, len(dft)):
        n = dft[i].get('freq')
        radius = dft[i].get('amp')
        phase = dft[i].get('phase')
        if(radius >= 1):
            pygame.draw.circle(screen, WHITE, [int(x), int(y)], int(radius), 1)
        else:
            pygame.draw.circle(screen, WHITE, [int(x), int(y)], 1, 1)
        temp_x = x
        temp_y = y
        x = x + radius * math.cos(n * time + phase + math.pi/2)
        y = y + radius * math.sin(n * time + phase + math.pi/2)
        pygame.draw.line(screen, WHITE, [temp_x, temp_y], [x, y])
        pygame.draw.circle(screen, WHITE, [int(x), int(y)], 0, 0)
                    
    if(not pause):
        wave.insert(0, [x, y])
        
        if(len(wave) > len(dft)):
            wave.pop()
    for i in range(1, len(wave)):
        pygame.draw.line(screen, PURPLE, wave[i - 1], wave[i])
    pygame.draw.line(screen, WHITE, [int(x), int(y)], wave[0])
    if(not pause):
        time -= tick
    pygame.display.flip()
pygame.quit()

